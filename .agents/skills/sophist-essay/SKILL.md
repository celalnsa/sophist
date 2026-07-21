---
name: sophist-essay
description: Use when turning the user's scattered memories, observations, voice transcripts, story notes, travel notes, daily scenes, moral reflections, or rough outlines into a reflective Chinese essay in the user's Sophist prose style.
---

# Sophist Essay

Use this for散文：偏回忆、记叙、旅行、人与事、生活场景，通过真实故事长出思想和情感。

For substantial drafting or evaluation, read:

- `../_sophist-writing/standards.md`
- `../_sophist-writing/evaluation.md`

## Core Standard

The essay must feel like a real person thinking from lived material. It should
not sound like fiction, a public-account essay, or a polished AI reflection.

Recent style has priority: rational, concise, reflective, and unwilling to say
empty beautiful things. Older pieces contribute scene, memory, film/book taste,
and emotional texture, not loose adolescent rhetoric.

Useful local samples:

- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2023-03-26-脐带.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2019-02-10-扫地.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2019-08-08-火车.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2018-09-04-苦瓜.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2018-11-07-梦旅人.md`

## Workflow

1. **Material gate**: list supplied facts/scenes, feelings, judgments, questions,
   and strong original phrases. Keep 3-8 raw phrases visible while drafting.
   Mark uncertain claims instead of smoothing them.
2. **Find the hidden question**: name the real pressure point. Example: not
   "猫绝育", but "人对自己造成的自然后果要不要负责？"
3. **Select anchors**: choose 1-3 true scenes or objects. If none exist, ask for
   one or write a shorter thought piece; do not invent a literary scene.
4. **Build the thinking order**: scene or observation -> first judgment ->
   tension or counter-thought -> deeper judgment -> image/open question. This
   is not a paragraph template. The finished essay should not make every scene
   serve an obvious thesis.
5. **Draft from the user's logic**: preserve their claims and emotional
   temperature. Expose instability instead of resolving it falsely.
6. **Cut hard**: remove route markers, generic transitions, moral slogans, and
   lines that only announce profundity. Prefer "我想到..." over "所以我会想到...".
   Cut one more sentence when a paragraph ends in a beautiful but replaceable
   sigh.
7. **Evaluate**: use `evaluation.md`; for a quick mechanical pass, optionally run
   `../_sophist-writing/scripts/evaluate_sophist_article.py --genre essay`.

## Quality Gate

- A true scene or lived detail appears near the beginning.
- The thought turns at least once; the essay is not pre-solved.
- Any Buddhist, philosophical, film, or book reference serves the thought rather
  than becoming a lecture.
- The ending can stand without "所以", "总之", or "归根结底".
- If the result sounds like tasteful generic prose, remove polish and recover
  the user's actual pressure point.

## Avoid

- Fictional characters, invented dialogue, or cinematic atmosphere not supplied
  by the user.
- Do not make the user "literary" or "poetic". The user demands grounded, sincere, pragmatic writing. Reject pretentious, high-flown minimalist posturing. A rough true scene is better than a pretty invented one.
- "这不仅是...更是...", "在这个时代", "复杂而微妙的张力", "我们每个人都应该".
- "看清这一点以后...", "怜悯变成责任", and similar emotional promotion unless
  the whole essay has earned that sentence.
- Public-account structure: phenomenon -> explanation -> emotional elevation ->
  "we should".
- Summary endings, inspirational endings, and neat moral closure.
- Decorative metaphors that do not carry reasoning.
