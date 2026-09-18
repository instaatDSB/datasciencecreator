## PAGE 30 — REUSABLE AI CODING TASK TEMPLATE

The single most useful thing you can copy out of this book is a template. Not a prompt template — a *task* template. Something you fill in before every meaningful change, until doing so becomes automatic and you no longer need the form.

Keep this template somewhere you can reach in ten seconds. Paste it into a note. Print it out. Whatever works.

---

**TASK TEMPLATE — AI CODING AGENT**

**TASK.**
*A one-line name for the change. Something you could tell a friend in an elevator.*
Example: *"Add a status filter to the Applications list."*

**GOAL.**
*The outcome, not the code. Why does this matter?*
Example: *"So the student can quickly see only the applications that are still active, without scrolling past rejected ones."*

**CONTEXT.**
*Which part of the project this touches. Point to the relevant folders, files, or existing patterns.*
Example: *"The Applications list page (`src/pages/applications/list.tsx`) and the shared status label component in `src/components/`."*

**INSPECT FIRST.**
*Ask the agent to look before it leaps.*
Example: *"Before proposing any changes, read the Applications list page and any file that touches application status. Summarize how status is stored and displayed today. Do not edit yet."*

**SCOPE.**
*What files or areas the agent may change.*
Example: *"The Applications list page and its stylesheet. Nothing else."*

**BOUNDARIES.**
*What must not change, and the standing safety rule.*
Example:
> *"Do not modify the database, the Add Application form, or any file outside `src/pages/applications/`. Do not add new libraries. If you believe another file must change, stop and tell me — do not change it yourself."*

**SUCCESS CRITERIA.**
*A short checkable list. What "done" looks like when a real person uses it.*
Example:
- *Filter buttons appear above the list.*
- *Clicking each filter shows only applications matching that status.*
- *"All" restores the full list.*
- *The Add Application flow still works exactly as before.*
- *The list still looks correct on a phone-sized screen.*

**VALIDATION.**
*How you (or the agent) will prove it works.*
Example:
- *Run the existing test suite. It must stay green.*
- *Manually filter by each status. Add one new application via the form and confirm it appears in the correct filter.*
- *Try one edge case: a status with zero applications. Confirm the list shows an empty state, not an error.*

**REVIEW.**
*What you will check before accepting the change.*
Example:
- *Only the scoped files were modified.*
- *No new dependencies were added.*
- *I can explain each hunk of the diff in one sentence.*
- *The change matches the success criteria above.*

---

Two things about this template.

First, filling it in should feel slow the first ten times and quick after that. If it feels slow forever, the task is probably ambiguous — which is exactly the moment when writing it down helps most.

Second, the template will change as your project changes. Add fields for the constraints that repeatedly bite you. Delete fields that never earn their keep. What you are really building, one task at a time, is a personal operating manual for how you work with agents. This template is only the starting shape.

---
