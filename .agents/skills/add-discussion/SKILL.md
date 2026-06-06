---
name: add-discussion
description: Use when adding a new philosophy discussion page to the Sophist archive, when asked about *how* to write one (voice, tone, 诗意, 思辨, avoiding AI-slop), when changing the site theme, or when building/previewing/deploying the site. Covers the content Markdown schema, the build step, theme consistency, and — most importantly — the prose temperament that defines this archive.
---

# Adding a discussion to Sophist

Sophist is a static archive: each philosophy discussion is one Markdown file in
`content/`, and `build.py` renders the whole folder into a themed site. The
whole point is that **a new page requires no HTML/CSS** — it inherits the theme.

> **Before writing anything: read the [写作的精神](#写作的精神最要紧的一节) section
> below.** The mechanics (frontmatter, build, theme) are easy. The voice is
> the whole point — without it this archive is just another blog.

## Add one discussion

1. `cp content/_example.md content/<slug>.md` — the slug becomes the URL
   (`<slug>.html`). Use a short kebab-case name, e.g. `free-will.md`.
   (Files whose names start with `_` are treated as templates and never published.)
2. Fill the frontmatter — only `title` is strictly required:

   | field | meaning |
   |---|---|
   | `title` | discussion title |
   | `source_ai` | which AI it came from (ChatGPT / Claude / Gemini / …) |
   | `date_discussed` | approx date, or `unknown` |
   | `themes` | list — powers index filter chips and aggregation |
   | `thinkers` | list of philosophers/schools referenced (`[]` if none) |
   | `abstract` | one or two sentences |
   | `status` | `settled` or `open` (renders as 已结 / 未决 pill) |

3. Write the body as plain Markdown. Recommended section headings (they render
   as styled uppercase `##` kickers): 缘起 / 核心问题, 关键概念, 论证脉络,
   高光片段, 暂时的结论, 悬而未决, 延伸. Use `>` blockquotes for highlight quotes.
4. Preview: `uv run python build.py --serve` → open http://localhost:8000
5. Commit + push to `main`. The GitHub Action rebuilds and redeploys to Pages.

These files pair with the user's **export prompt** (run inside other AIs) which
already emits exactly this frontmatter + section structure — paste its output
straight into a new `content/*.md`.

## Build commands

- `uv run python build.py` — build into `_site/`
- `uv run python build.py --serve` — build, then serve `_site/` on :8000
- Dependencies are declared in `pyproject.toml` (`markdown`, `python-frontmatter`, `jinja2`).

## Changing the theme (keep all pages consistent)

Do **not** add per-page styles. Edit:

- `theme/theme.css` — palette + typography are CSS variables at the top
  (`--ink`, `--paper`, `--brass`, `--display`, `--body`…). Change once, the
  whole archive follows.
- `templates/base.html` — masthead/footer/`<head>` shared by every page.
- `templates/index.html` — the 目录 (landing) page + theme filter chips.
- `templates/discussion.html` — the per-discussion layout + `.prose` styling
  for rendered Markdown.

Keep the temperament: dark background, classical serif display (Fraunces) +
literary body (Newsreader), one warm-brass accent, generous space, restrained
motion — an intellectual / 哲思 feel.

## The writing bar (non-negotiable — set by the user)

This is an archive of *thought*, not a summary dump. Each piece must:

- **Be a real essay, not a template.** Do NOT use a fixed 缘起/关键概念/论证脉络/结论
  scaffold — that reads utilitarian and 世俗. Let structure grow from the idea.
  Minimum is title + flowing content.
- **Stage two voices genuinely arguing** (a dialectic in one head), and expand /
  deepen the thought rather than restate it. It's fine to go beyond a source export.
  But this is a *style cue*, not a constraint — don't force two voices when the
  thought wants a single steady stream, or three voices, or none. Form follows idea.
- **Be poetic and restrained.** Titles like 「解药即毒药」「燃料」「不争」「未经同意的降生」
  — short, paradoxical, 留白; never paper-like or colloquial or AI-slop.

Markdown helpers available in the literary template (write as raw HTML inside the .md,
with a blank line around each block):

- `<p class="lede">…</p>` — opening line, set larger in display serif.
- `<p class="counter">…</p>` — the counter-voice (brass left-rule, italic).
- `<p class="pull">…</p>` — a centered pull-line.

When a topic deserves its own form/feel, make it a bespoke `.html` (see
`system-as-fuel.html` 燃料, `non-contention.html` 不争, `pharmakon.html`) — own
layout, palette, even interactions. Give it its own accent so it has an identity.

## 写作的精神（最要紧的一节）

这是 Sophist 的灵魂。前面是脚手架，这一节是温度。形式可以全然自由，但下面这点
"魂"，无论用什么形式，都要在。

### 一、不说"禅"，是禅意才在

讲禅意最远的，恰恰是张嘴就说"禅"的那一种。

**别这么写：**
> 这与禅宗讲的"无常"是一回事——人是流动的，不该被一张快照困住。
> 老子说"夫唯不争，故天下莫能与之争"——真正的力量在不争。
> 佛说"一切皆苦"，这恰恰是接受的开始。

凡是"这与…是一回事""如…所言""佛说…""禅宗讲…"这一类，都是在每句诗后面贴说明牌——
道理被点破的同时，意思就漏光了。读者来这里不是听人转述前人的结论的；他要的是
和那个道理在文字里**当场相遇一次**。

**该这么写**——让形象自己说话，让读者自己撞见：

> 河上的船夫，最不轻易跟人说"那条河是什么样的"。今早他撑船过去，水深三尺；
> 中午回来，水深两尺；傍晚再去，水里多了一群鱼。

无常这两个字，从头到尾没出现，可它就在那条河里。

老子、庄子、佛陀、苏格拉底——这些名字像香料，不是不能撒，是不能当饭吃。
偶尔出现一句原典做锚（比如《道德经》一句"水善利万物而不争"放在合适的位置），
有力量；句句都贴一张"这就是…"的标签，就成了 PPT。

判断标准很硬：**写完后通读，凡是"这就是XX""这恰恰是XX""如XX所言"这类句式，
默认先划掉，看看划掉之后段落是不是反而更亮**。十次有九次是的。

### 二、形象先于命题

要表达一个道理，先去找它的**具象支点**——一个画面、一个动作、一个小故事、
一个微观的人。形象立住了，道理自己就会从形象的背后渗出来。命题立在前面，
形象只是去解说它，文章就死了。

仓库里这些具象支点都是这么找的：
- "斧头会被换，可知道砍哪棵树的眼睛不会"——讲 AI 时代剩下的是判断。
- "种树的人只管挖坑、培土、浇水，至于何时开花是风的事、雨的事"——讲因上尽力、果上随缘。
- "井底之蛙抬头看天，它说的是它真看见的——只是把'我看见的'说成了'整个的'"——讲"唯一"。
- "替钱守夜的攒钱人——门越锁越多，能在夜里出去走走的人越来越少"——讲老去的收缩。
- "握刀的人，多半正觉得自己在主持公道"——讲无知之恶。

找形象的小窍门：**把抽象动词改成具体动作**。"被困住"→"住进了驿站"。"看见情绪"→
"风过竹林，竹子会响"。"放下执着"→"船过水面，水分开又合上"。

### 三、留白比讲透重要

不要把每个意思都讲到底。讲到八分，剩下两分让读者自己走进去——这两分是属于读者的，
也是文章和读者之间最深的连接。

具体地：
- 一个段落里，最关键的那一句**之后**应该停。不要再补一句"换句话说…"或"也就是说…"。
- 一篇文章的结尾，**不要总结全文**。让最后一个形象/最后一句格言式的话自己落地——
  像一颗石子掉进水里，余波归读者。
- 段落之间允许跳跃。读者比我们想象的聪明——他自己会接上中间那一步。

**别这么收尾：**
> 所以综上所述，意义不是被发现的，而是被做出来的。这就是萨特存在主义的核心，
> 也是我们今天最需要的态度。

**该这么收尾：**
> 没有人来告诉他这是值得的——他在弯腰、插秧、看雨、晒粮的那些年里，自己就把
> "值得"两个字，一颗一颗种下去了。
>
> 意义不写在天上，它写在你做过的事里。

最后那一句几乎像偈语，但前面一整段田里的画面已经把它撑住了。

### 四、避开 AI 腔

这是最难也最具体的一条。AI 腔的本质是**信息密度太高 + 修辞过密 + 起承转合太工整**——
读起来像是被某个模板生成的，没有呼吸。

**最明显的几种 AI 病**（看见就要警惕）：

- **三联排比 / 节奏复读机**："不是 X，不是 Y，是 Z" "既是…又是…还是…"用一两次有
  力，用多了就成了腔调。一段里不要超过一次。
- **过度对仗**："光与影""生与死""得与失""庙与灯"——对仗一旦密集，就成了对联工厂。
  人写的句子是不齐的，有长有短，有时还故意失重。
- **"它不过是…它其实是…"句式**：这种"先抑后扬"在一篇里出现一次是亮点，出现三次
  就是套路。
- **形容词堆砌**："这是一种深刻、复杂、又微妙的张力"——三个形容词一起上，多半是
  没想清楚。删到一个，常常更准。
- **"在 X 时代/在 X 的世界里"开头**：太多次了。换种法。
- **"恰恰""恰恰相反""恰恰是…"**：偶尔用，提神；逢段必用，就是 GPT。
- **过度的"也许""可能""或许"**：人写东西会先选一边，再去打磨；不会句句加缓冲垫。

**怎么写得像人：**

- **句子要长短交错**。长句之后一定要跟一句短的、断的、甚至是不完整的。一段
  全是 25 字以上的句子，读着就喘。看一眼现在仓库里的篇章，几乎每段都有一句
  极短的——三五个字，戛然而止。那是呼吸口。
- **允许重复一个词**。AI 倾向于每次换个词以显得丰富；人会同一个词反复用，因为
  那个词是这段的钉子。
- **允许"不完美"的口语**。"那问题是什么。""可是退到哪里去呢。""老木匠手里有一把斧头。"
  这种简单的开头比工整的"于是问题转化为：…"要人得多。
- **偶尔用一个意外的、半生不熟的比喻**。AI 喜欢那种"安全的、被验证过的"比喻
  （像水、像火、像河、像光）。这些可以用，但混进去一两个不寻常的——
  "它不是石头，是一段还在播放的影像""门越锁越多，能在夜里出去走走的人越来越少"——
  那是人在场的证据。

### 五、思想自由，立场可偏

放飞——不要预设"我"代表人、"AI"代表机器，不要预设两个声音必须势均力敌。

- 哪一边对就站哪一边。两个声音可以**不均衡**——有时第二个声音只是给第一个声音
  补一刀，然后被驳回；有时反过来。
- 也可以**两个声音都错**，第三种视角才是落点。
- 也可以**只有一个声音**——一个人在自己里面想清一件事，没必要假装在对话。
- 也可以**没有声音**——就是一段叙述、一个故事、一段独白。

唯一不能的是：**为了对称而对称**。"一个声音说A，另一个声音说B，于是中道是C"——
这种套路写多了就成了模板，是 AI 腔的另一种症状。让张力是真的张力，不是表演。

### 六、温度，是这一切的总和

最后一条没法量化，只能感觉：

读自己写完的一段，问自己——**这句话，会不会有一个真正在想这件事的人，
在深夜的桌前，把它一笔一笔写下来？** 如果答案是"不会，这话太工整、太流畅、
太知道自己在说什么"，那就重写。

最高级的笔触，是看起来像有人在迟疑、在自言自语、在边写边想——
而不是在交付一份"高质量答案"。AI 最容易掉进的陷阱，是把每段都写得完美。
人不完美，所以人写的东西也带着一丝粗砺。这丝粗砺，恰恰是最贵的东西。

### 七、形式不被任何上面这些约束

以上全是关于温度与味道，**不是关于形式**。形式应当全然自由：

- 可以是两个声音的辩论，可以是独白，可以是一封信，可以是一个短故事，
  可以是几行散文诗，可以是一组分镜，可以是问答。
- 可以一句话一段，也可以一千字一气呵成。
- 可以有小标题（参考的 `## 缘起/关键概念/…` 只是历史习惯，不是规定），
  也可以从头到尾不分段。
- 一篇值得自己长相的，就做成 bespoke HTML——自己的字体、自己的配色、
  自己的小交互（参见 `pharmakon.html` 的解药↔毒药切换、`non-contention.html`
  的圆相、`system-as-fuel.html` 的火色 + 两声部）。

要记住的只是上面那六条**精神**：
不说禅 / 形象先于命题 / 留白 / 避 AI 腔 / 思想自由 / 温度。

形式怎么样都可以，只要这六条还在。

## YAML pitfall (this WILL bite)

A frontmatter value (esp. `title`/`abstract`) must **not start with an ASCII `"`** —
YAML reads it as a quoted scalar and the build crashes. Use fullwidth quotes “ ” or
「 」 instead. Same for `.html` files' `<!--sophist ... -->` metadata block.
