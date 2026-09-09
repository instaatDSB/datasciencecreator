# Editorial Audit — THE AI CODING AGENT PLAYBOOK

Audit date: 2026-09-09
Auditor: Editorial QA pass, six-phase review.

## Overall verdict

Publication-ready. The manuscript delivers on its promise: it teaches beginners
to build a workflow around AI coding agents, not to hunt for better prompts.
Voice is consistent, the Student Job Tracker holds together as one evolving
example, and the reader is walked through a coherent narrative from confusion
to a usable operating system.

## Strengths

- **Voice.** Calm, senior-technical-educator register maintained across all pages.
  Reads like a real book, not a blog post.
- **Running example.** The Student Job Tracker stays small and familiar. It
  evolves believably from "add a status" through "add a filter" without any
  contradictory architectural detail.
- **Narrative arc.** CONFUSION → RECOGNITION → UNDERSTANDING → MENTAL MODEL →
  PRACTICE → CONTROL → CONFIDENCE → INDEPENDENCE lands where it needs to.
- **Core thesis** ("prompt ≠ workflow") is stated, dramatized, and paid off —
  not merely asserted.
- **Framework consistency.** The 8-stage operating system (DEFINE → CONTEXT →
  INVESTIGATE → BOUNDARIES → EXECUTE → VERIFY → REVIEW → LEARN) is introduced
  on Page 7, referenced throughout, codified on Page 28, walked through on
  Page 29, and repeated on the reference card. No competing frameworks appear.

## Weaknesses reviewed and resolved

### 1. Framework inconsistency
Earlier drafts split between a 7-stage version (BOUNDARIES rolled into EXECUTE)
and an 8-stage version (BOUNDARIES as its own stage). Adopted the **8-stage**
version canonically per the master brief. Page 7 now previews it that way; Page
28 codifies it; the reference card mirrors it.

### 2. "Blast radius" callback
The concept appears twice — briefly on Page 10, in full on Page 18. Page 18
now opens with an explicit callback to Page 10, so the second appearance reads
as depth, not a duplicate introduction.

### 3. Absolute-language creep
Softened three claims that risked becoming false:
- Page 5's comparison table hedged "what the agent can see" to "as much of your
  codebase as you allow, and as its context window permits."
- Page 12's list of memory-file names now explicitly says filenames will keep
  shifting; the habit matters more than any one product name.
- Page 22's type-checker line now says "many of these mismatches," not "all."

### 4. Junior-developer analogy
Appears twice (Pages 4 and 6). Left in deliberately — it is the load-bearing
analogy of the book and the second use extends it (the contractor variant)
rather than restating it. No further duplication in later chapters.

## Beginner accessibility

Every technical term introduced in the manuscript is defined in-line the first
time it appears, and again in the Glossary (Appendix). Explicit in-line
glosses now exist for:

- **codebase** (Page 15)
- **diff** (Page 24)
- **test** — both manual and automated (Page 21)
- **build** (Page 22)
- **schema** (Page 26, inside the rules example)
- **dependency / library** (Page 26)
- **AGENTS.md and similar files** (Pages 11 and 12) — framed as project memory,
  not tool-specific

Glossary now contains 40+ entries, including all beginner terms named in the
master brief: AI coding agent, repository, codebase, dependency, API,
component, authentication, authorization, environment variable, database,
migration, test, unit test, integration test, linting, type checking, build,
deployment, diff, refactoring, architecture, production, configuration.

## Technical accuracy

Reviewed every technical claim. Notable adjustments:

- **Tests are not proof of correctness.** Page 23 states this plainly and Page
  24 reinforces it in the context of diff review.
- **Type checking hedged.** Not every mismatch is caught by every type checker.
- **Memory file behavior hedged.** "Most modern tools read that file at the
  start of a session; the exact behavior varies."
- **No absolute AI claims** ("AI always…", "agents understand…") remain.

## Repetition

Deliberate reinforcement kept:
- **"prompt ≠ workflow"** — Ch. 1 states it, Ch. 6 dramatizes, Ch. 14
  operationalizes, Ch. 28 codifies, Ch. 32 closes on it.
- **"controlled autonomy"** — Ch. 17 introduces, Ch. 25 sharpens, Ch. 32 seals.
- **"look before you leap"** — Ch. 14 introduces, Ch. 15 details, Ch. 29 shows.

Each recurrence adds a layer; none is a copy-paste of an earlier passage.

## Pages that received the most revision

- **Page 7** — reconciled with Page 28's operating system (8 stages, matching
  order and names).
- **Page 18** — added a callback to Page 10.
- **Pages 30–32** — written fresh (task template, checklists, closing).

## Editorial callouts

Selective and purposeful. KEY IDEA, BEGINNER NOTE, WATCH OUT, REAL-WORLD
EXAMPLE, TRY THIS, REMEMBER — each used only where it earns its place. No
page carries decorative callouts.

## Final status

**COMPLETE — publication-ready.**
