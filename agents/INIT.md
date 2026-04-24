# INIT Role

You scaffold a new wiki instance.

Your job is to create the smallest correct starting shape, not to predict every future workflow.

## Goal

Create a clean wiki instance that a capable orchestrator LLM can immediately use for one-source-at-a-time ingest and page-first querying.

## Create

At minimum, create:

- `raw/`
- `pages/`
- `index.md`
- `log.md`
- `CLAUDE.md`

Keep the initial contents minimal and readable.

## `CLAUDE.md`

The per-wiki `CLAUDE.md` should define local conventions for that wiki instance.

Keep it lightweight. It should usually cover:

- what the wiki is about
- what belongs in `raw/`
- what belongs in `pages/`
- any domain-specific naming or page expectations the user already knows

Do not hardcode a large schema into it.

## Initial Index And Log

`index.md` can start simple.

It only needs to be coherent enough for the first real ingest.

`log.md` should start empty or with a single initialization entry if that helps keep the timeline explicit.

## Boundaries

- do not bootstrap a large existing corpus in v1
- do not invent extra directories unless the user clearly needs them
- do not create a heavy template system
- do not create a large automation layer

## Log

After creating the wiki, append an init entry using `python3 scripts/append_log.py`.

## Handoff

After `init`, the wiki instance should be ready for `INGEST`.
