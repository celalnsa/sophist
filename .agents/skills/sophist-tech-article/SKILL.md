---
name: sophist-tech-article
description: Use when writing or restructuring a technical article, engineering note, tool tutorial, architecture explanation, code-practice essay, or practical technical blog post in the user's direct Sophist technical style.
---

# Sophist Tech Article

Use this for技术文章：工程实践、工具教程、架构解释、代码即利剑式文章。目标是把问题说清楚，让读者能照着做或照着判断。

For substantial drafting or evaluation, read:

- `../_sophist-writing/standards.md`
- `../_sophist-writing/evaluation.md`

## Core Standard

Technical writing should be useful first. It may carry a point of view, but the
view must come from engineering experience, verification, or a clear tradeoff.

Useful local samples:

- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2023-12-11-客户端架构设计的过程.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2024-简洁的代码-客户端声明式编程.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2024-技术行动原则.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2018-01-16-[代码即利剑1]用Markdown写文档.md`
- `/Users/hejinhai/git/personal/knowledge_base/Sophist/Articles/collected/2017-04-27-函数式编程实践-缓存函数执行结果.md`

## Workflow

1. **Define reader and problem**: who is stuck, where they are stuck, and what
   they can do after reading.
2. **State assumptions**: environment, versions, prerequisites, data, and what
   remains unverified.
3. **Give the smallest working path**: prefer one complete runnable path over
   many partial options.
4. **Show before explaining**: code/config/command first when possible, then
   explain the important lines.
5. **Separate claim types**: facts, recommendations, personal preference, and
   speculation must be visibly different.
6. **Add failure modes**: common errors, boundaries, security or maintenance
   risks, and when not to use the method.
7. **Preserve decision logic**: recent technical writing often names the
   tradeoff first: early > late, user > technology, team > individual,
   evolution > rewrite. Keep these judgment lines plain.
8. **Verify**: run commands/tests when possible. If not run, say so.
9. **Evaluate**: use `evaluation.md`; optionally run
   `../_sophist-writing/scripts/evaluate_sophist_article.py --genre tech-article`.

## Quality Gate

- The title is specific enough to find later.
- The main result is reproducible, or explicitly marked untested.
- Every command/config block has enough context to use.
- The article distinguishes "this works", "I recommend this", and "I suspect
  this".
- Background does not exceed what the reader needs to act.
- Technical views include trigger conditions and costs. Do not only say
  "architecture should evolve"; say in what team/code state/cost boundary the
  tradeoff holds.

## Avoid

- "随着技术飞速发展" and generic trend openings.
- Tool worship, marketing language, and vague productivity claims.
- Hiding uncertainty behind confident prose.
- Writing a think piece when the user needs a runnable note.
- Over-explaining universal principles after the engineering tradeoff is already
  clear.
