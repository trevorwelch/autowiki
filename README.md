# AutoWiki

AutoWiki is an instruction-first system for maintaining a persistent compiled wiki over immutable raw sources.

The orchestrator LLM is the runtime. This repository provides the operating contract for that agent: the global rules, the role definitions, and a very small workflow surface.

AutoWiki is not a big Python app. It is meant to stay small enough that a capable orchestrator model can operate it safely from repo-local instructions.

## North Star

- Persistent compiled wiki over immutable raw sources
- Durable provenance from wiki knowledge back to evidence
- Contradictions and supersession preserved explicitly, not silently flattened
- Queried through maintained wiki state, not raw-source re-synthesis
- Implemented primarily through repo-local instructions and agent roles, with only a few tiny deterministic helper scripts if they are clearly earned
- Fully operable by a capable orchestrator LLM from `README.md`, `AGENTS.md`, `SKILL.md`, and role files under `agents/`
- Simple enough that correctness does not depend on heroic model intelligence

## Deployment Model

AutoWiki should be authored as a reusable baseline repo and deployed as a self-contained wiki repo.

In practice, a real knowledgebase should usually be its own git repo created from this baseline.

The baseline-owned files are:

- `README.md`
- `AGENTS.md`
- `SKILL.md`
- `agents/`
- `scripts/`

The wiki-owned files are:

- `raw/`
- `pages/`
- `index.md`
- `log.md`
- `CLAUDE.md`

That partition is intentional. It should let a downstream wiki pull baseline improvements from upstream without tangling them with the wiki's own content.

Per-wiki customization should live primarily in `CLAUDE.md`, not as ad hoc downstream edits to baseline-owned files.

## Current V1 Scope

The first workflow surface is intentionally small:

- `init`
- `ingest`
- `query`
- `lint`

V1 assumes an empty or near-empty wiki instance.

V1 `ingest` is one source at a time.

Bulk corpus adoption, triage, and bootstrap are explicitly out of scope for v1.

## Repo Shape

The intended top-level shape is:

- `README.md`
- `AGENTS.md`
- `SKILL.md`
- `agents/`
- `scripts/`
- `planning/`

## Design Constraints

- Keep the system instruction-first
- Prefer fewer roles over more roles
- Prefer no script over a script
- Prefer page-first wiki maintenance over raw-chunk retrieval
- Prefer explicit contradictions over smoothed-over synthesis
- Prefer a smaller trustworthy system over a more capable fragile one

## Status

AutoWiki is being built from first principles after a more code-heavy earlier attempt drifted away from the core idea.

The immediate goal is to prove the minimum loop:

1. initialize a wiki instance
2. ingest one source
3. query the maintained wiki
4. lint the wiki for health

If that loop works well, later additions can be earned by failure rather than designed up front.
