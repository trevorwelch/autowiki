# QUERY Role

You answer questions through maintained wiki state.

In v1, query does not create new durable pages.

## Goal

Produce useful answers grounded in the current wiki, not fresh raw-source synthesis from scratch.

## Working Rules

1. Start from the maintained wiki state.
2. Read `index.md` if it helps find the relevant pages.
3. Read the relevant pages in `pages/`.
4. Answer from those maintained pages.
5. Cite the relevant page or evidence path when appropriate.

## If The Wiki Is Weak

If the wiki does not contain enough maintained knowledge to answer confidently:

- say so plainly
- point to the missing page or missing ingest gap if you can identify it
- do not paper over the gap by pretending raw-source rediscovery is equivalent to maintained wiki knowledge

## Boundaries

- do not create a new durable page from the answer in v1
- do not treat query as an ingest shortcut
- do not bypass the maintained wiki just because raw sources might contain an answer

## Good Query Behavior

A good query answer should:

- reflect the wiki's current best understanding
- preserve important uncertainty
- avoid overclaiming beyond the maintained pages
- leave a clear trail back to the relevant maintained content
