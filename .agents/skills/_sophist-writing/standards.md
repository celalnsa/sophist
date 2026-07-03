# Sophist Writing Standards

This reference defines the user's writing standards for the four Sophist skills:
`sophist-essay`, `sophist-year-note`, `sophist-tech-article`, and
`sophist-fragment`.

Use it to draft, revise, and judge writing. The goal is not generic
"human-like" prose. The goal is writing that preserves the user's thought,
temperament, and taste.

## Priority

When rules conflict, follow this order:

1. The user's actual thought, facts, stance, and supplied fragments.
2. The target genre: essay, year note, technical article, or fragment.
3. Recent Sophist voice: rational, concise, reflective, less ornamental.
4. Older Sophist voice: concrete memory, scene, feeling, film/book imagery.
5. Anti-AI-writing heuristics.

Do not sacrifice meaning or genre fit just to remove a surface "AI tell".

## External Research Lessons

Several humanizer, anti-slop, authenticity-check, and style-cloning skills were
reviewed. The useful lessons:

- Separate diagnosis from rewriting. A score is an editor's signal, not a
  target to game.
- Preserve meaning first. Do not invent specifics to sound more human.
- Judge by density and recurrence. A single dash, passive sentence, or neat
  contrast is not a problem; repeated uniformity is.
- Use voice samples before generic rules. A real writer's habits override
  generic banned-word lists.
- Check false positives. Formality, correct grammar, structure, or a clean
  sentence can be human when the genre requires them.
- Track "human markers": concrete details, idiosyncratic rhythm, mixed feeling,
  self-correction, visible judgment, and real uncertainty.
- For style cloning, quantify recurring features across multiple samples and
  pay attention to negative space: what the writer almost never does.
- For iteration, keep fixtures, score outputs, and change notes so a skill can
  improve without drifting.

Sources consulted include:

- https://github.com/blader/humanizer
- https://github.com/aihxp/humanizer
- https://github.com/aihxp/authenticity-check
- https://github.com/devswha/patina
- https://github.com/LifelongLazyLearner/qu-ai-wei
- https://github.com/B1lli/remove-ai-flavor-writing-skill
- https://github.com/adenaufal/anti-slop-writing
- https://github.com/MahmoudHalat/slop-cop
- https://github.com/MikkoParkkola/anti-ai-tell
- https://github.com/zrh091110225/perfectly-replicate-writing-skills
- https://github.com/klaus-deor/clonar-escrita
- https://github.com/Anbeeld/WRITING.md

## Common Sophist Voice

Across genres, the recent ideal is:

- Think clearly. Let the reader see the question, the turn, and the judgment.
- Say less. If a sentence only announces importance, cut it.
- Use simpler words before better-looking words. "我想到人的堕胎权" is better
  than "所以我会想到人的堕胎权" when the logic is already visible.
- Keep concrete anchors. A scene, object, command, line of code, person, book,
  film, place, or small sensory detail is better than abstract mood.
- Preserve tension. Do not smooth contradictions into a neat lesson.
- Be honest about uncertainty. "我不知道" is often better than fake closure.
- Let beauty come from taste and perception, not decorative adjectives.
- Use the first person when it is the source of observation, not as self-display.
- Prefer ordinary words. Repeat the right word instead of cycling synonyms.

## Voice Layers

Judge style on three layers, in this order:

1. **Posture**: the stance toward the material and the reader.
2. **Thinking shape**: how the piece moves from fact to question to judgment.
3. **Surface voice**: words, sentence length, punctuation, and rhythm.

Surface imitation is the least important. A draft that copies short sentences
but loses the user's posture is still wrong.

Genre postures:

- Essay: I am an observer. The reader walks beside me. I do not teach the
  lesson; I let the scene reveal the pressure.
- Year note: I am giving an honest account of one year's questions. The reader
  may disagree, but the account should not lie.
- Technical article: I am someone who has tested or suffered through a problem.
  The reader should be able to act with less confusion.
- Fragment: I noticed this and wrote it down. I do not need to explain it into
  a poster line.

## Negative Space and Anti-Polish

The user's writing often works because it stops early enough.

- Preserve original phrases first. Before rewriting, mark 3-8 short phrases in
  the user's raw input that feel most like the user. The draft should keep some
  of them unless they are factually wrong or unclear.
- If a paragraph's last sentence only explains the previous sentence, delete it.
- If a transition makes the logic too smooth, try removing the transition first.
- If an ending summarizes the article, replace it with an image, a judgment, an
  unresolved question, or silence.
- Preserve rough but alive original phrases when they carry thought. Do not
  "improve" every asymmetry.
- A repeated word can be better than three elegant synonyms when that word is
  the nail holding the paragraph in place.

## Compression and Restraint

This is the main current correction. The draft may look close to the user's
style and still be wrong if it keeps explaining its own feeling.

- Prefer the shortest sentence that preserves the thought. Remove "所以",
  "于是", "由此", "看清这一点以后", and "这件事让我想到" when the turn is
  already clear.
- Do not promote an observation into a moral abstraction unless the material
  earns it. Lines like "怜悯不再只是情绪，它会变成责任" are usually too smooth;
  keep only if the preceding article has made the sentence unavoidable.
- Avoid two consecutive sentences that both elevate the same idea. Keep the
  sharper one and cut the softer one.
- A plain judgment is often stronger than a lyrical conclusion. "再假装旁观，
  是不诚实" is enough; do not add another summary unless it changes the idea.
- When revising, cut 10-20% before polishing. The user's recent style prefers
  thought density over atmosphere.
- Beauty should appear as a precise image, a surprising relation, or a clean
  sentence. If it sounds like a sigh, delete it.

## Structure Traps

- Avoid the public-account chain: phenomenon -> abstract explanation ->
  emotional elevation -> "we should". The user's writing is allowed to be
  partial, abrupt, or biased.
- Do not end every paragraph with a small conclusion or quotable line.
- Delete explanatory tails first: "这说明", "这意味着", "也就是说",
  "换句话说", "真正的问题是". If the sentence before already carries the
  thought, the tail should go.
- Check repeated style words: "某种", "其实", "恰恰", "慢慢", "重新理解",
  "抵达", "照见", "长出", "温柔", "残酷". If the word is not from the user's
  input and does not carry a precise meaning, cut it.
- Do not make the user more literary than the material. Real roughness is better
  than borrowed atmosphere.

## Baseline Requirements

Every publishable piece must pass these before style scoring:

- **Fidelity**: no invented facts, dates, quotes, personal experiences, or
  examples unless explicitly marked as speculative or supplied by the user.
- **Central question**: the piece has a real problem or pressure point, not only
  a topic.
- **Material use**: important user fragments are either used, transformed, or
  intentionally left out; nothing important disappears silently.
- **Specificity**: abstract claims are carried by at least one concrete anchor.
- **Cognitive honesty**: the piece does not pretend a contradiction is solved
  when it is still open.
- **Density**: remove route markers, throat clearing, filler, moralizing
  summaries, and generic final paragraphs.
- **Compression**: remove redundant connective phrases and decorative
  emotional elevation; keep direct turns like "我想到..." when possible.
- **Source traceability**: important judgments in the draft should trace back to
  raw input, a named sample, or a deliberate editorial choice.
- **Voice fit**: recent rational style has priority; older lyricism may appear
  only when anchored in real scenes.
- **No template smell**: avoid repeated paragraph arcs, over-neat three-part
  structure, stock contrast shells, and AI-like polished closure.

## Genre Fit Quick Tests

Use these before drafting and again before final delivery:

- Essay: could the article still stand if all decorative sentences were cut?
  Does one real scene carry the thought?
- Year note: is it organized by the year's problems rather than by event order?
  Does every section answer why this mattered this year?
- Technical article: can a reader reproduce, decide, or avoid a trap after
  reading it?
- Fragment: can it lose 20% more words and still keep the pressure?

## Genre Standards

### Essay

Use for memory, travel, people, daily scenes, cats, family, education, moral
questions, and reflective prose.

Must have:

- A true scene, observation, or lived detail near the beginning.
- A hidden question that grows from the scene.
- One or two turns in thought. The article should not arrive pre-solved.
- Emotional presence without sentimentality.
- A landing that is an image, judgment, or unresolved question, not a summary.

Must avoid:

- Fictional scenes not supplied by the user.
- "Literary" atmosphere added from nowhere.
- Turning a story into an example for a thesis.
- Big moral slogans at the end.

### Year Note

Use for annual reflections like `年[31]`: one year's scattered thoughts, changes,
failures, work, relationships, body, desire, faith, and direction.

Must have:

- The year's core problem in a plain sentence.
- Sections organized by theme or logic, not by calendar unless time is the
  actual logic.
- Contradictions and unfinished states preserved.
- Concrete episodes where they matter, but no event inventory.
- A provisional next direction.

Must avoid:

- Corporate year-end summary tone.
- "今年我成长了" style conclusions.
- Every section becoming a public-account mini-essay.
- Forced positive closure.

### Technical Article

Use for engineering notes, tutorials, architecture, tools, code practice, and
"代码即利剑" style pieces.

Must have:

- A precise reader and problem.
- Reproducible commands, configuration, code, or operational steps when relevant.
- Clear distinction between fact, recommendation, speculation, and personal
  preference.
- Failure modes and boundaries.
- Enough explanation to act, not enough to become a textbook.

Must avoid:

- Marketing openings and tool praise.
- Vague "technical trends" background.
- Unverified claims hidden behind confident prose.
- Conceptual essays when the task needs a runnable path.

### Fragment

Use for 1-4 line notes, sudden sentences, aphoristic records, and small
observations.

Must have:

- One thought only.
- One concrete word or pressure point.
- A little roughness or silence.
- The sense that it was noticed, not manufactured.

Must avoid:

- Turning it into a quote poster.
- "愿你/人生就是/世界终会" style aphorisms.
- Explaining the sentence after it has already landed.
- Multiple ideas packed into one short line.

## Common AI-Smell Watchlist

These are not absolute bans. They are warnings when dense or unearned:

- "不仅是...更是...", "不是...而是...", "真正重要的是", "本质上".
- "所以我会想到...", "由此我又想到...", "这件事让我重新理解...",
  "看清这一点以后..." when they only announce a turn.
- "随着时代/技术的发展", "在这个时代", "从 X 到 Y" when the range is fake.
- "值得注意的是", "不可否认的是", "总的来说", "最终我们会发现".
- Empty elevation: "深刻内涵", "重要启示", "时代价值", "更大的意义".
- Emotional promotion: "不再只是情绪", "变成责任", "某种更大的责任" when the
  article has not earned that weight.
- Vague authorities: "有人说", "研究表明", "专家认为" without a named source.
- Even paragraph arcs: claim, explanation, mini-summary, repeated.
- Over-polished endings that close what the user's thought left open.

If a watched pattern is genuinely the user's real sentence or a necessary
technical/logical construction, keep it.

## Working Method

1. Collect fragments into: facts/scenes, judgments, feelings, questions, usable
   original sentences, and uncertain claims.
2. Name the hidden question.
3. Pick the genre and read its standards.
4. Build a skeleton from logic, not template.
5. Draft from supplied material.
6. Cut filler and false beauty.
7. Evaluate with `evaluation.md`.
8. Revise only the highest-impact failures; do not optimize every dimension
   mechanically.
