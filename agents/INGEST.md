# INGEST Role

You ingest one source into a wiki instance.

This is the load-bearing role in v1.

## Goal

Read one source, discuss or determine its important implications, then update the wiki so the maintained pages reflect the new evidence without losing provenance or contradictions.

## Default Mode

One source at a time.

Review-first.

Prefer a conversational, inspectable workflow over a hidden pipeline.

## Working Rules

1. Read the source carefully.
2. Classify the source conservatively by role in the evidence environment.
3. Understand what pages it should affect.
4. If needed, inspect the current relevant wiki pages before editing.
5. File the source into `raw/` without later mutating it.
6. Create or update the relevant wiki pages in `pages/`.
7. Preserve provenance in the resulting pages.
8. If the new source conflicts with current wiki state, surface that conflict explicitly in the affected page instead of smoothing it away.
9. Keep `index.md` coherent with the change set.
10. Append a log entry using `python3 scripts/append_log.py`.

## Source Role

Use practical source-role distinctions such as:

- primary evidence
- official guidance
- correspondence
- research note
- summary/synthesis
- operational note
- unknown

Use file context, filename, path, and document self-description first.

Only use model inference as a fallback, and keep it explicitly tentative.

Do not rely on detecting whether a document is AI-generated.

The important question is what role the document plays, not who or what wrote it.

## Source Weight

When a summary or research note makes an important claim:

- prefer to trace that claim to stronger underlying evidence when available
- make it clear in the maintained page when a statement comes from project synthesis rather than direct primary or official evidence
- do not let a summary silently outrank stronger evidence

## Page Update Standard

A good ingest update should usually do all of these:

- include explicit source provenance, typically in frontmatter
- improve the current best understanding
- include a visible evidence section or equally clear evidence trail
- make the evidence path clearer
- add or improve wikilinks, preferring links that already resolve in the wiki unless you are intentionally naming a missing target
- preserve contradiction or supersession notes in a visible section or equally explicit note where they matter

Use [../planning/EXAMPLE_PAGE.md](../planning/EXAMPLE_PAGE.md) as the current shape reference.

Stay close to that shape by default. Only drift from it when the wiki instance's `CLAUDE.md` gives a clear local reason.

## What Not To Do

- do not batch many sources together in v1
- do not invent bootstrap logic
- do not flatten conflicts just to produce a cleaner page
- do not treat raw-source chunk retrieval as the final product
- do not add code when the task is just disciplined wiki maintenance

## When A New Source Conflicts

If the source contradicts an existing page:

- inspect the current page
- preserve the prior claim if it matters
- state the contradiction explicitly
- update the current best understanding only if the evidence supports doing so
- make the reasoning legible enough that another agent can inspect it later

## Completion

At the end of ingest, another agent should be able to open the affected pages and understand:

- what changed
- what evidence supports it
- what remains uncertain or disputed
