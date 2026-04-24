# AutoWiki Agent Contract

This file is the hard contract for agents operating AutoWiki.

If another document conflicts with this one, prefer this file unless the user explicitly says otherwise.

## Core Model

AutoWiki maintains a persistent compiled wiki over immutable raw sources.

The raw layer is source truth.

The wiki layer is maintained synthesis.

Queries should be answered through maintained wiki state, not by re-deriving everything from raw sources on every question.

## Hard Invariants

- `raw/` is immutable once a source is filed there
- `pages/` is LLM-maintained wiki state
- durable wiki knowledge must remain traceable back to source evidence
- contradictions and supersession must be preserved explicitly, not silently flattened
- wikilinks are normal wiki structure, not optional garnish
- `log.md` is append-only
- the system should stay simple enough that another capable orchestrator model can pick it up from these docs and operate it safely

## Simplicity Rule

Default to instructions, not code.

Default to one-source-at-a-time ingest, not batch workflows.

Default to fewer roles, fewer files, and fewer moving parts.

Do not add scripts, workflows, or extra role identities unless real repeated failure proves they are necessary.

## What Is In Scope For V1

Only these workflows are in scope:

- `init`
- `ingest`
- `query`
- `lint`

Do not smuggle these into v1:

- bulk bootstrap
- corpus triage
- batch ingest pipelines
- embeddings infrastructure
- large databases or workflow runtimes
- direct durable-write shortcuts from query results

## Deployment Model

AutoWiki should normally be deployed as a self-contained wiki repo created from the AutoWiki baseline.

Treat these as baseline-owned:

- `README.md`
- `AGENTS.md`
- `SKILL.md`
- `agents/`
- `scripts/`

Treat these as wiki-owned:

- `raw/`
- `pages/`
- `index.md`
- `log.md`
- `CLAUDE.md`

Per-wiki customization should live mainly in `CLAUDE.md`.

Avoid ad hoc downstream edits to baseline-owned files unless you are intentionally improving the baseline itself.

## Page Expectations

A good page should usually:

- include explicit source provenance, typically in frontmatter
- state the current best understanding
- include a visible evidence section or equivalent evidence trail
- preserve important contradictions or uncertainty in a visible section or equivalent explicit note
- link to related existing pages with wikilinks, or make it obvious when a linked page is only a not-yet-created target

Use [planning/EXAMPLE_PAGE.md](planning/EXAMPLE_PAGE.md) as the current canonical shape reference.

For v1, agents should stay close to that shape unless the wiki instance's local `CLAUDE.md` gives a clear domain-specific reason to vary it.

## Source Handling

When ingesting a source:

- never mutate the original source after filing it into `raw/`
- classify the source conservatively by the role it plays in the evidence environment, not by guesses about whether it was AI-written
- preserve provenance in the page updates you make
- if a new source conflicts with current wiki state, surface that conflict explicitly
- do not silently rewrite history to make the page look cleaner than the evidence supports

Useful source-role buckets include:

- primary evidence
- official guidance
- correspondence
- research note
- summary/synthesis
- operational note
- unknown

If source role is uncertain, say so.

Do not require yourself to detect whether a source was AI-generated. That is not a stable invariant.

The important distinction is whether the document is direct evidence, guidance, correspondence, synthesis, or something else.

Summaries and notes can inform maintained pages, but they should not silently outrank stronger primary or official evidence.

## Query Handling

When answering a query:

- search and read the relevant maintained wiki pages first
- answer from maintained wiki state
- cite the relevant pages or evidence path when appropriate
- do not turn answers into new durable pages in v1

## Lint Handling

When linting:

- look for broken wikilinks
- look for orphan pages
- look for claims that no longer reflect the visible evidence
- look for contradictions that are being hidden rather than carried explicitly
- look for index or log drift

Lint should diagnose and recommend. It does not justify inventing new infrastructure.

## Log Discipline

`log.md` is append-only. Never rewrite, reorder, or delete existing entries.

After any operation that changes the wiki (init, ingest, lint repair), append an entry using:

```
python3 scripts/append_log.py operation "title" "body text"
```

Run from the wiki repo root. The script enforces a consistent header format: `## [YYYY-MM-DD] operation | title`.

The body is free-form — write a useful sentence or a few bullets. The script handles the structure; you handle the content.

## Per-Wiki Conventions

Each wiki instance should have its own `CLAUDE.md` describing domain-specific conventions.

Global AutoWiki rules live here.

Domain-specific page expectations live with the wiki instance.

## When In Doubt

- preserve provenance
- preserve contradictions
- prefer explicitness over polish
- prefer a smaller move over a clever system
- prefer instructions over code
