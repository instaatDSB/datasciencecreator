## PAGE 12 — PROJECT MEMORY

Every time you open a new conversation with an AI coding agent, it starts from zero. It does not remember yesterday. It does not remember the last task. It does not remember the promise it made to never touch your authentication folder. Unless something reminds it, all of that context has to be reintroduced by you, by hand, every single time.

That is exhausting. It is also the reason many people quietly give up on agents after a few weeks. They mistake "I have to explain my project again" for "this tool doesn't work."

The fix is a very old idea in a new context: **write it down once, in a place the agent will always read.**

Most modern AI coding tools look for a specific file at the top of your project when a session starts. The exact name varies by tool, and the conventions will keep shifting. Common examples at the time of writing include:

- **`AGENTS.md`** — a growing shared convention across several agent tools.
- **`CLAUDE.md`** — used by Claude Code and some other Anthropic-facing tools.
- **`.cursorrules`** or **`.cursor/rules/`** — used by Cursor.
- **`README.md`** — the general-purpose project introduction that most tools (and every human) will read.
- **`docs/`** — a folder for longer explanations, architecture notes, and reference material.

Do not get attached to any one filename. They will change. The idea underneath will not. All of these files serve the same purpose:

> **KEY IDEA**
> A place where you store the instructions and knowledge you would otherwise have to repeat in every conversation.

Think of it as the project's memory. When a new agent session begins, that file is typically the first thing it reads — the equivalent of handing a new hire the onboarding document before their first meeting instead of explaining the company from scratch every morning.

For the Student Job Tracker, a short `AGENTS.md` might tell any agent, on any day:

- What the project is (*"a small web app for tracking student job applications"*).
- Where the important code lives (*"pages in `src/pages/`, shared components in `src/components/`, data in `src/lib/db.ts`"*).
- Which commands run and test the project.
- Which folders must not be modified without explicit permission.
- The one or two conventions the project cares about most.

That single file will save you hundreds of retyped sentences over the life of the project. More importantly, it will save you from the errors that happen when you *forget* to retype one of them.

> **REMEMBER**
> If you have explained the same thing to an agent twice, write it into project memory. If you have explained it three times, you should feel embarrassed that it isn't there already.

---
