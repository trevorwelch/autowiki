# AutoWiki Skill

This file defines the smallest initial AutoWiki workflow surface.

It is intentionally narrow.

## Purpose

AutoWiki helps a capable orchestrator LLM maintain a persistent compiled wiki over immutable raw sources.

The agent should use these workflows to operate on a wiki instance, not to build a separate application layer around it.

## V1 Workflows

### `init`

Use `init` to scaffold a new wiki instance.

Expected outcome:

- a new wiki directory exists
- it contains `raw/`, `pages/`, `index.md`, `log.md`, and a per-wiki `CLAUDE.md`
- the initial structure is simple and ready for one-source-at-a-time ingest

Route to: `agents/INIT.md`

### `ingest`

Use `ingest` to process one source into an existing wiki instance.

Expected outcome:

- the source is filed into `raw/`
- relevant wiki pages are created or updated in `pages/`
- provenance is preserved
- page structure stays close to the canonical example shape unless the wiki's local conventions clearly say otherwise
- contradictions are surfaced explicitly if the new source conflicts with current wiki state
- `index.md` and `log.md` are kept coherent with the changes

Route to: `agents/INGEST.md`

### `query`

Use `query` to answer a question through maintained wiki state.

Expected outcome:

- the agent reads the relevant wiki pages
- the answer is grounded in maintained wiki content
- the answer does not become a new durable page in v1

Route to: `agents/QUERY.md`

### `lint`

Use `lint` to check wiki health.

Expected outcome:

- identify structural or knowledge-maintenance issues
- recommend repairs or follow-up ingest/questions
- avoid turning lint into a new subsystem

Route to: `agents/MAINTAINER.md`

## Explicitly Deferred

Do not add these to the skill surface in v1:

- `triage`
- `bootstrap`
- batch ingest
- query promotion
- rectifier as a separate dedicated workflow
- embeddings workflows
- MCP-specific behavior

## Operating Discipline

- prefer instruction-only operation first
- only add deterministic helper scripts after repeated real failures
- keep the command vocabulary small
- prove the core loop on real use before expanding it
