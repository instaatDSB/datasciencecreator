## PAGE 26 — TURN MISTAKES INTO RULES

Every time you work with an AI coding agent, something small goes wrong. The agent modifies a file it should not have. It invents a function name that doesn't exist. It picks a library you don't use. It "cleans up" code you liked the way it was. It over-refactors. It renames things without being asked.

Beginners react to each of these moments in isolation. They fix it, they sigh, they move on, and next week the same thing happens again. That is the trap.

Serious users of AI coding agents do something different, and it is the habit that eventually separates people who ship reliable software from people who chase the same bugs forever. They turn each recurring mistake into a **rule**, and they write the rule into a place the agent will read every time.

The loop is simple:

**MISTAKE → RULE → BETTER FUTURE BEHAVIOR**

You notice the mistake. You write a sentence that would have prevented it. You add that sentence to your project's memory — the `AGENTS.md`, `CLAUDE.md`, or equivalent file we talked about earlier. From that point on, every new session starts with that lesson already in place.

A few concrete examples, all drawn from the kinds of things beginners actually run into with a project like the Student Job Tracker.

> **REAL-WORLD EXAMPLE**
>
> **Problem:** The agent repeatedly modifies files outside the feature you asked about.
> **New rule:** *"Do not modify files outside the feature under discussion unless explicitly required. If you believe an outside file must change, stop and ask."*
>
> **Problem:** The agent keeps adding new libraries (external packages of pre-written code you install into a project) to solve small problems.
> **New rule:** *"Do not add new dependencies without explicit approval. Prefer solutions using the libraries already in `package.json`."*
>
> **Problem:** The agent quietly changes the database schema — the shape of the database, meaning which fields exist and what type each one is — when adding features.
> **New rule:** *"Never change the database schema in the same task as a UI change. Schema changes require their own task and their own review."*
>
> **Problem:** The agent writes tests only for the happy path.
> **New rule:** *"When adding a new feature, include at least one test for an edge case — empty input, missing field, or unexpected value."*
>
> **Problem:** The agent invents function names or files that don't exist.
> **New rule:** *"Before referring to a function or file, confirm it exists by searching the codebase. Do not assume."*

Each rule is short, specific, and written in the imperative. Each one closes a door that has been quietly slammed on you at least once. Together, over weeks and months, they turn your project memory from a generic onboarding document into something much more valuable: a record of the specific, hard-earned lessons this project has taught you.

> **TRY THIS**
> At the end of any session that produced a surprise, ask: *"What sentence, added to project memory, would have prevented this?"* Then add the sentence. That single question, asked honestly and often, is the difference between an agent that gets worse to work with over time and one that gets better.

---
