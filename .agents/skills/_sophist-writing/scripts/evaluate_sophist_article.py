#!/usr/bin/env python3
"""Strict-ish audit for Sophist writing drafts.

This script has two separate scores:

- lint_score: cheap hygiene checks. A high lint score only means no obvious
  surface smell was found.
- strict_score: a conservative iteration score. It estimates how much room the
  draft still has before it feels like the user's own writing.

Neither score is a final judge. The strict score is intentionally hard to max
out and always requires human review.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path


AI_PATTERNS = [
    ("not_only_but", r"不[仅只]是.{0,24}(更是|还是|也是|而是)"),
    ("not_x_but_y", r"(不是|并非|不在于).{0,24}(而是|而在于)"),
    ("true_essence", r"真正(重要|决定|关键|打动人|有意义).{0,12}(是|在于)"),
    ("essentially", r"本质上"),
    ("era_opening", r"随着.{0,18}(发展|进步|深入|变化|普及)"),
    ("in_this_era", r"在这个时代|在当今.{0,8}时代"),
    ("we_will_find", r"最终我们会发现"),
    ("overall", r"总的来说|综上所述|归根结底"),
    ("undeniable", r"不可否认|值得注意"),
    ("empty_elevation", r"深刻内涵|重要启示|时代价值|复杂而微妙"),
    ("emotional_promotion", r"不再只是.{0,8}情绪|会变成责任|更大的责任"),
    ("redundant_turn", r"所以我会想到|由此我又想到|看清这一点以后|这件事让我重新理解"),
    ("moralizing_we", r"我们每个人都应该"),
]

ROUTE_MARKERS = [
    "下面我们", "接下来", "我们可以看到", "希望这能", "让我们", "本文将",
    "综上所述", "总而言之", "划重点", "说白了", "所以我会", "由此我又",
]

CONCRETE_HINTS = [
    r"\d", r"[A-Za-z][A-Za-z0-9_+-]*", "猫", "火车", "房子", "酒", "辣",
    "肉肠", "电影", "书", "代码", "命令", "老师", "学生", "父母", "孩子",
    "风", "沙子", "花", "芒果", "旅行", "睡觉",
]

FILLER_WORDS = [
    "然后", "就是", "这个", "那个", "其实", "所以", "但是", "因为", "的话",
    "我觉得", "我想", "一个", "一些", "这样", "那样", "可能", "应该",
]

ABSTRACT_TERMS = [
    "意义", "生命", "灵魂", "责任", "文明", "自由", "自然", "世界", "关系",
    "整体", "本能", "意识", "选择", "系统", "能力", "情绪", "重量", "价值",
]

SOFT_STYLE_WORDS = [
    "某种", "慢慢", "重新理解", "抵达", "照见", "长出", "温柔", "复杂",
    "微妙", "更大的", "真正", "不再只是",
]

SUMMARY_ENDING_PATTERNS = [
    r"我们.*(连在一起|成为|意识到|应该|需要)",
    r"(先看|看见|看清).*(改变|回应|责任|重量)",
    r"(这就是|这接近|也接近).{0,20}(意义|责任|灵魂|无众生相)",
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            return parts[1]
    return text


def split_paragraphs(text: str) -> list[str]:
    body = strip_frontmatter(text)
    paragraphs = []
    for raw in re.split(r"\n\s*\n", body):
        p = raw.strip()
        if not p or p.startswith("#"):
            continue
        paragraphs.append(p)
    return paragraphs


def split_sentences(text: str) -> list[str]:
    pieces = re.split(r"(?<=[。！？!?；;])\s*|\n+", text)
    return [p.strip() for p in pieces if p.strip()]


def count_regex_occurrences(text: str, patterns: list[tuple[str, str]]) -> dict[str, int]:
    hits: dict[str, int] = {}
    for name, pattern in patterns:
        count = len(re.findall(pattern, text))
        if count:
            hits[name] = count
    return hits


def count_occurrences(text: str, patterns: list[str]) -> dict[str, int]:
    return {p: text.count(p) for p in patterns if text.count(p)}


def has_concrete_hint(paragraph: str) -> bool:
    return any(re.search(pattern, paragraph) for pattern in CONCRETE_HINTS)


def sentence_cv(sentences: list[str]) -> float | None:
    if len(sentences) < 3:
        return None
    lengths = [len(re.sub(r"\s+", "", s)) for s in sentences]
    mean = statistics.mean(lengths)
    if mean == 0:
        return None
    return statistics.pstdev(lengths) / mean


def compact_text(text: str) -> str:
    body = strip_frontmatter(text)
    body = re.sub(r"(?m)^#+\s+.*$", "", body)
    for word in FILLER_WORDS:
        body = body.replace(word, "")
    return re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]+", "", body)


def source_phrase_retention(source_text: str, draft_text: str) -> dict:
    """Estimate how many raw source phrases survived the transformation.

    This is deliberately simple. It should not force copy-paste, but it catches
    drafts that convert every rough user phrase into generic smooth prose.
    """

    source = compact_text(source_text)
    draft = compact_text(draft_text)
    if not source or not draft:
        return {"rate": None, "found": 0, "sampled": 0, "examples": []}

    candidates: list[str] = []
    for size in (10, 8, 6):
        if len(source) <= size:
            starts = [0]
        else:
            max_samples = 45
            step = max(size // 2, (len(source) - size) // max_samples)
            starts = range(0, len(source) - size + 1, step)
        for i in starts:
            phrase = source[i : i + size]
            if phrase and phrase not in candidates:
                candidates.append(phrase)
    sampled = candidates[:120]
    found = [phrase for phrase in sampled if phrase in draft]
    rate = len(found) / max(1, len(sampled))
    return {
        "rate": rate,
        "found": len(found),
        "sampled": len(sampled),
        "examples": found[:8],
    }


def count_terms(text: str, terms: list[str]) -> int:
    return sum(text.count(term) for term in terms)


def ending_summary_flag(paragraphs: list[str]) -> bool:
    if not paragraphs:
        return False
    ending = paragraphs[-1]
    return any(re.search(pattern, ending) for pattern in SUMMARY_ENDING_PATTERNS)


def score_strict(
    *,
    text: str,
    source_text: str | None,
    genre: str,
    lint_score: int,
    paragraphs: list[str],
    sentences: list[str],
    concrete_count: int,
    ai_hits: dict[str, int],
    route_hits: dict[str, int],
    uniform_rhythm: bool,
    long_paragraphs: list[int],
    gflags: list[str],
) -> dict:
    """Return a conservative writing-iteration score and failure list.

    100 means close to indistinguishable from a strong user-authored piece, not
    merely "good prose". The default posture is strict; high lint cannot buy a
    high strict score.
    """

    body = strip_frontmatter(text)
    body_chars = len(re.sub(r"\s+", "", body))
    source_chars = len(re.sub(r"\s+", "", strip_frontmatter(source_text))) if source_text else None
    ratio = body_chars / source_chars if source_chars else None
    phrase_stats = source_phrase_retention(source_text, text) if source_text else None
    abstract_count = count_terms(body, ABSTRACT_TERMS)
    soft_count = count_terms(body, SOFT_STYLE_WORDS)
    concrete_ratio = concrete_count / max(1, len(paragraphs))

    failures: list[str] = []
    caps: list[tuple[int, str]] = []
    score = 25

    # Hygiene helps, but cannot dominate the real writing score.
    score += min(10, max(0, lint_score - 50) // 5)

    if source_text:
        retention_rate = phrase_stats["rate"] or 0
        if retention_rate < 0.08:
            failures.append("原始短语保留太少：可能把真实口语压力翻译成了顺滑散文")
            caps.append((68, "原始短语保留过低"))
        elif retention_rate < 0.16:
            failures.append("原始短语保留偏少：需要找回几句更像用户自己的表达")
            caps.append((76, "原始短语保留偏低"))
        score += min(12, int(retention_rate * 75))

        if ratio is not None:
            if ratio > 0.85:
                failures.append("压缩不足：语音输入整理后仍接近原长度，说明解释尾巴还多")
                caps.append((70, "压缩不足"))
                score += 3
            elif ratio < 0.42:
                failures.append("压缩过度风险：可能丢掉原始材料里的犹豫和细节")
                caps.append((74, "压缩过度风险"))
                score += 4
            else:
                score += 8
    else:
        failures.append("缺少原始输入：无法判断材料转化，只能做表面审计")
        caps.append((45, "缺少原始输入"))

    if concrete_ratio >= 0.55:
        score += 10
    elif concrete_ratio >= 0.35:
        score += 7
    else:
        score += 3
        failures.append("具体材料承重不足：抽象判断多于真实场景")

    abstract_density = abstract_count / max(1, body_chars / 1000)
    soft_density = soft_count / max(1, body_chars / 1000)
    if abstract_density > 22:
        failures.append("抽象词密度过高：概念可能盖过材料")
        caps.append((72, "抽象词密度过高"))
    elif abstract_density < 12:
        score += 6
    else:
        score += 4

    if soft_density > 5:
        failures.append("软性风格词偏多：容易出现温柔、成熟、公共号式表达")
        caps.append((76, "软性风格词偏多"))
    else:
        score += 6

    if uniform_rhythm:
        failures.append("节奏过匀：段落和句子像被整理得太平")
        caps.append((74, "节奏过匀"))
    else:
        score += 5

    if long_paragraphs:
        failures.append("长段落仍需拆解或压缩：" + ",".join(map(str, long_paragraphs[:5])))
    else:
        score += 4

    if ai_hits or route_hits:
        failures.append("仍有表面 AI/路线词信号，需要逐个确认")
    else:
        score += 5

    if ending_summary_flag(paragraphs):
        failures.append("结尾仍有总结/升华腔，应该落在更具体的判断或留白")
        caps.append((72, "结尾总结腔"))
    else:
        score += 5

    if genre == "essay":
        if paragraphs and has_concrete_hint(paragraphs[0] + (paragraphs[1] if len(paragraphs) > 1 else "")):
            score += 5
        if len(paragraphs) > 20:
            failures.append("段落数量偏多：可能每个想法都被解释了一遍")
            caps.append((72, "段落数量偏多"))
        else:
            score += 4
    elif genre == "fragment":
        score += 5 if body_chars <= 220 else 0
    elif genre == "year-note":
        score += 5 if len(re.findall(r"(?m)^##\s+", text)) >= 3 else 0
    elif genre == "tech-article":
        score += 5 if re.search(r"(代价|条件|风险|边界|验证|测试)", text) else 0

    if gflags:
        failures.extend(gflags)
        score -= min(8, len(gflags) * 3)

    cap = min([88, *[item[0] for item in caps]])
    strict_score = max(0, min(cap, int(score)))
    if strict_score >= 80:
        failures.append("80+ 需要人工复核：确认不是靠卫生分和流畅度抬高")

    return {
        "strict_score": strict_score,
        "score_cap": cap,
        "score_caps": [{"cap": c, "reason": r} for c, r in caps],
        "manual_review_required": True,
        "top_failures": failures[:8],
        "source_chars": source_chars,
        "draft_chars": body_chars,
        "draft_source_ratio": ratio,
        "source_phrase_retention": phrase_stats,
        "abstract_term_count": abstract_count,
        "soft_style_word_count": soft_count,
        "strict_note": (
            "Strict score is a conservative iteration score, not a detector. "
            "90+ should be rare and requires human review against source and samples."
        ),
    }


def genre_flags(genre: str, text: str, paragraphs: list[str], sentences: list[str]) -> list[str]:
    flags: list[str] = []
    if genre == "fragment":
        body_chars = len(re.sub(r"\s+", "", strip_frontmatter(text)))
        if body_chars > 220:
            flags.append("fragment_too_long")
        if len(sentences) > 5:
            flags.append("fragment_too_many_sentences")
    elif genre == "tech-article":
        if "```" not in text and not re.search(r"\b(uv|npm|go|python|curl|git|make|juex)\b", text):
            flags.append("tech_missing_command_or_code_signal")
        if not re.search(r"(验证|测试|运行|结果|失败|边界|注意|错误|风险)", text):
            flags.append("tech_missing_verification_or_boundary_signal")
    elif genre == "year-note":
        heading_count = len(re.findall(r"(?m)^\s*(#{2,6}\s+|\d+[.、]\s*)", text))
        if heading_count < 3:
            flags.append("year_note_missing_sections")
        if re.search(r"(首先|其次|最后).{0,20}(收获|成长)", text):
            flags.append("year_note_corporate_summary_smell")
    elif genre == "essay":
        if paragraphs and not has_concrete_hint(paragraphs[0] + (paragraphs[1] if len(paragraphs) > 1 else "")):
            flags.append("essay_opening_lacks_concrete_anchor")
        if re.search(r"(总之|所以我们应该|最终我们会发现|这告诉我们)", paragraphs[-1] if paragraphs else ""):
            flags.append("essay_summary_ending")
    return flags


def audit(path: Path, genre: str, source_path: Path | None = None) -> dict:
    text = path.read_text(encoding="utf-8")
    source_text = source_path.read_text(encoding="utf-8") if source_path else None
    paragraphs = split_paragraphs(text)
    sentences = split_sentences(strip_frontmatter(text))
    ai_hits = count_regex_occurrences(text, AI_PATTERNS)
    route_hits = count_occurrences(text, ROUTE_MARKERS)
    concrete_count = sum(1 for p in paragraphs if has_concrete_hint(p))
    cv = sentence_cv(sentences)
    uniform_rhythm = cv is not None and cv < 0.32 and len(sentences) >= 6
    long_paragraphs = [i + 1 for i, p in enumerate(paragraphs) if len(re.sub(r"\s+", "", p)) > 280]
    gflags = genre_flags(genre, text, paragraphs, sentences)

    penalty = 0
    penalty += min(20, sum(ai_hits.values()) * 2)
    penalty += min(15, sum(route_hits.values()) * 3)
    penalty += 8 if uniform_rhythm else 0
    penalty += min(12, len(long_paragraphs) * 3)
    penalty += min(15, len(gflags) * 5)
    if paragraphs and concrete_count / max(1, len(paragraphs)) < 0.25:
        penalty += 10

    lint_score = max(0, 100 - penalty)
    strict = score_strict(
        text=text,
        source_text=source_text,
        genre=genre,
        lint_score=lint_score,
        paragraphs=paragraphs,
        sentences=sentences,
        concrete_count=concrete_count,
        ai_hits=ai_hits,
        route_hits=route_hits,
        uniform_rhythm=uniform_rhythm,
        long_paragraphs=long_paragraphs,
        gflags=gflags,
    )
    return {
        "file": str(path),
        "genre": genre,
        "lint_score": lint_score,
        "mechanical_score": lint_score,
        **strict,
        "paragraph_count": len(paragraphs),
        "sentence_count": len(sentences),
        "sentence_length_cv": cv,
        "concrete_paragraph_count": concrete_count,
        "ai_pattern_hits": ai_hits,
        "route_marker_hits": route_hits,
        "uniform_rhythm_flag": uniform_rhythm,
        "long_paragraphs": long_paragraphs,
        "genre_flags": gflags,
        "note": "lint_score is only hygiene; strict_score is conservative and still requires manual review.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--source", type=Path, help="Raw input or source notes used to produce the draft")
    parser.add_argument("--genre", choices=["essay", "year-note", "tech-article", "fragment"], required=True)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    result = audit(args.path, args.genre, source_path=args.source)
    if args.pretty:
        print(f"Strict score: {result['strict_score']}/100")
        print(f"Lint score: {result['lint_score']}/100")
        print(f"Paragraphs: {result['paragraph_count']}, sentences: {result['sentence_count']}")
        print(f"Concrete paragraphs: {result['concrete_paragraph_count']}")
        if result.get("draft_source_ratio") is not None:
            print(f"Draft/source ratio: {result['draft_source_ratio']:.2f}")
        if result.get("source_phrase_retention"):
            stats = result["source_phrase_retention"]
            print(f"Source phrase retention: {stats['found']}/{stats['sampled']} ({stats['rate']:.2%})")
        if result["ai_pattern_hits"]:
            print("AI pattern hits:", result["ai_pattern_hits"])
        if result["route_marker_hits"]:
            print("Route marker hits:", result["route_marker_hits"])
        if result["uniform_rhythm_flag"]:
            print("Uniform rhythm: yes")
        if result["long_paragraphs"]:
            print("Long paragraphs:", result["long_paragraphs"])
        if result["genre_flags"]:
            print("Genre flags:", result["genre_flags"])
        if result["top_failures"]:
            print("Top failures:")
            for failure in result["top_failures"]:
                print(f"- {failure}")
        print(result["note"])
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
