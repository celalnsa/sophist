# Sophist Writing Evaluation

Use this reference to score drafts produced by the Sophist writing skills and
to iterate on the skills themselves.

The score is a disciplined editorial estimate, not a detector. Do not rewrite
only to raise the number. The point is to make the article closer to the user's
thinking and taste.

## Fatal Failures

If any fatal failure appears, stop and fix it before scoring:

- Invented personal experience, source, date, quote, technical fact, or example.
- Major user claim reversed, softened beyond recognition, or silently dropped.
- Wrong genre: a fragment became an essay, a technical article became a think
  piece, an essay became fictional prose, or a year note became a diary list.
- Text is generic enough that it could belong to any thoughtful person.
- Technical article contains actionable commands or claims that were not checked
  or marked unverified.

## Score Overview

Total: 100.

Common score: 80. Genre score: 20.

Important: separate two scores.

- `lint_score` is a hygiene check. It only catches cheap surface signals such
  as AI phrases, route markers, missing concrete anchors, and uniform rhythm.
  A 100 lint score means almost nothing by itself.
- `strict_score` is the iteration score. It must be conservative, source-aware,
  and capped when core failures remain. It should leave room for improvement:
  a clean but still-too-smooth draft can sit around 50-70.

Run strict scoring with the raw input whenever possible:

```bash
python .agents/skills/_sophist-writing/scripts/evaluate_sophist_article.py \
  --genre essay \
  --source /path/to/raw-input.md \
  /path/to/draft.md
```

Pass bands:

- 90-100: Publishable or close; only taste-level edits remain.
- 80-89: Good draft; fix 1-2 visible weaknesses.
- 70-79: Strong direction, but still has visible voice or structure issues.
- 50-69: Usable skeleton; useful material is present, but the draft is still
  too smooth, too explanatory, or too far from the raw voice.
- 30-49: Early draft. The thought is visible but the skill did not preserve the
  user's pressure well enough.
- Below 30: Rebuild the skeleton, not just sentences.

90+ should be rare. It requires raw material, a draft, a source trace, and human
review. Do not give 90+ because a script has no complaints.

## Common Score (80)

### 1. Fidelity and Material Use (15)

- 13-15: Preserves user facts, stance, and important fragments; transforms rough
  input without losing its pressure.
- 9-12: Mostly faithful; a few important fragments are underused or blurred.
- 0-8: Invents, drops, or over-smooths core material.

### 2. Central Question and Thought Spine (15)

- 13-15: A real hidden question drives the piece; each paragraph moves the
  thought forward.
- 9-12: Topic is clear but the argument sometimes stalls or becomes modular.
- 0-8: No spine; it is a collection of nice statements.

### 3. Sophist Voice Fit (15)

- 13-15: Recent rational, concise, reflective voice leads; older lyricism is
  used only as concrete memory or taste.
- 9-12: Some passages sound right, but parts are too generic or too polished.
- 0-8: Sounds like a public writing assistant, not the user.

### 4. Concrete Anchors and Beauty (10)

- 9-10: Concrete scenes/objects/details carry abstract claims; beauty feels
  observed, not decorated.
- 6-8: Has anchors but leans too much on abstraction.
- 0-5: Mainly abstract mood, theory, or ornament.

### 5. Reasoning, Tension, and Honesty (10)

- 9-10: Shows uncertainty, contradiction, or friction where the material has it.
- 6-8: Reasoning is clear but too neat.
- 0-5: Moralizes, declares, or resolves too quickly.

### 6. Density and Concision (10)

- 9-10: Few wasted sentences; no throat clearing; every paragraph earns space.
- 6-8: Some filler, repeated explanations, or soft transitions.
- 0-5: Bloated, ceremonial, or over-explained.

Extra penalty inside this dimension:

- Deduct when the draft repeatedly uses connective padding such as "所以我会",
  "由此我又想到", "看清这一点以后".
- Deduct when a paragraph ends by upgrading a clear observation into empty
  emotion, for example "不再只是情绪，它会变成责任".
- Deduct when deleting 10% of explanatory sentences makes the article stronger.
- Deduct when the draft loses the raw input's rough but recognizable phrases.

### 7. Structure and Rhythm (8)

- 7-8: Shape fits the genre; paragraph weight and sentence rhythm have human
  variance without fake mess.
- 4-6: Readable but too even or too template-like.
- 0-3: Mechanical outline or shapeless flow.

### 8. Anti-AI Texture (7)

- 6-7: No dense AI-smell patterns; no generic uplifting final paragraph.
- 3-5: A few repeated shells or polished assistant moves remain.
- 0-2: Obvious AI texture: formulaic contrasts, route markers, generic elevation.

## Genre Score (20)

### Essay

- 5: Starts from a real scene or observation.
- 5: The story and thought are interwoven; neither dominates mechanically.
- 5: Emotional force is present but restrained.
- 5: Ending lands on image/judgment/open question, not summary.

### Year Note

- 5: Names the year's core problem plainly.
- 5: Sections are logical, not calendar inventory.
- 5: Contradictions and unfinished states are preserved.
- 5: Ends with a practical provisional direction.

### Technical Article

- 5: Reader/problem is explicit.
- 5: Steps, commands, code, or architecture are reproducible or marked untested.
- 5: Fact/recommendation/speculation are separated.
- 5: Failure modes and boundaries are included.

### Fragment

- 5: One thought only.
- 5: Has a concrete word, image, or pressure point.
- 5: Leaves silence; does not explain itself.
- 5: Reads found, not manufactured.

## Mechanical Audit

Before or after manual scoring, run:

```bash
python .agents/skills/_sophist-writing/scripts/evaluate_sophist_article.py \
  --genre essay \
  --source path/to/raw-input.md \
  path/to/draft.md
```

Supported genres: `essay`, `year-note`, `tech-article`, `fragment`.

The script reports both `lint_score` and `strict_score`. Treat `lint_score` as a
spell-checker. Treat `strict_score` as a conservative reviewer that can still be
wrong. Human judgment still assigns the final score.

Strict scoring should cap high scores when these remain:

- raw phrase retention is too low;
- source-to-draft compression is too weak or too extreme;
- abstract concepts cover the concrete material;
- the ending summarizes or elevates the piece;
- paragraph structure is too even.

## Role Separation

When iterating skills, split roles:

- Evaluator: only scores and names failures. Does not write the draft.
- Skill author: only changes rules to address repeated failures.
- Writer: only drafts from raw input using the skill. Does not score itself.

The main agent may integrate results, but should not let a generated draft pass
because the generator likes its own work.

## Iteration Protocol

Use this loop whenever improving the skills:

1. Save raw input, skill version, generated draft, score, and top 3 failures.
2. Only edit a skill for repeated or high-impact failures, not one taste
   disagreement.
3. After editing, rerun at least:
   - the two existing `Sophist/test/*.md` voice-input examples;
   - one older article-inspired prompt;
   - one new blind prompt if available.
4. Accept the change only if:
   - average score rises by at least 5, or
   - a target failure disappears without lowering fidelity.
5. Record the main cut ratio when a draft feels close but too lyrical. A useful
   revision should often become shorter before it becomes prettier.
6. Record what changed and why. Keep old scores; do not rewrite history.

Recommended log location:

```text
/Users/hejinhai/git/personal/sophist/.tmp/sophist-writing-evals/
```

## Evaluation Output Format

When asked to evaluate, report:

```markdown
## Score
Genre: essay
Strict score: 58/100
Lint score: 96/100
Band: Usable skeleton

## Breakdown
- Fidelity and Material Use: 13/15
- Central Question and Thought Spine: 12/15
...

## Top Fixes
1. ...
2. ...
3. ...

## Skill Feedback
- If this failure repeats, update `sophist-essay` by ...
```
