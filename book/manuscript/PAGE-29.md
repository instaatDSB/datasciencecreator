## PAGE 29 — REAL-WORLD WALKTHROUGH

To make the operating system concrete, here is one realistic task in the Student Job Tracker, worked all the way through. The task is small, deliberately. A small task, done well, teaches the workflow more clearly than a large task done impressively.

**The task, as it might first appear in your head:**
*"Add a filter to the dashboard so I can see only the applications with a given status."*

Watch how that sentence becomes real work through the eight stages.

**1. DEFINE**
You write, before doing anything else:

> *Objective:* Let the student narrow the Applications list to a single status at a time.
> *Scope:* The Applications list page only.
> *Expected result:* A row of buttons above the list — All, Active, Rejected, Offer, Withdrawn. Clicking one shows only applications matching that status. "All" restores the full list.
> *Constraints:* No new libraries. No changes to the database. No changes to the Add Application form.
> *Done means:* Each button filters correctly, "All" returns everything, existing add/edit flows still work, the list still looks correct on a phone-sized screen, existing tests still pass.

**2. CONTEXT**
You confirm that project memory (`AGENTS.md`) already covers the project structure, commands, and off-limits folders. You do not repeat this in the task; the agent will read it.

**3. INVESTIGATE**
Your first instruction to the agent is not "add the filter." It is:

> *"Before proposing any changes, read the Applications list page and any component or function that already touches application status. Summarize how status is stored and displayed today, and where you think the filter should live. Do not edit any files yet."*

The agent reports back that status is already stored on each application, already displayed as a colored label, and that the list page fetches all applications at once and renders them in a simple component. It proposes putting the filter buttons above the list and filtering in memory. You agree.

**4. BOUNDARIES**
Your next instruction:

> *"Change only the Applications list page and its stylesheet. Do not modify the data layer, the Add Application form, or any file outside `src/pages/applications/`. If you believe another file must change, stop and tell me."*

**5. EXECUTE**
You ask for the change in two small steps rather than one:

> *"Step 1: Add the filter buttons above the list. Have 'All' be selected by default. Do not wire them up to any filtering logic yet. Stop when done."*

You look at the result. The buttons are there. Nothing else moved.

> *"Step 2: Wire the buttons so clicking one filters the visible list to that status. Keep the current filter selection in the page's local state. Do not persist it."*

You look again. The filter works.

**6. VERIFY**
You run the project's tests: green. You open the app manually. You click each status button in turn — the list narrows correctly. You click "All" — everything comes back. You add a new application with status "Rejected" using the existing form (which you did not want to change) — it saves, and the "Rejected" filter now includes it. You resize the browser to a phone width — the buttons wrap cleanly, the list still reads well.

You also try an edge case: a status with zero applications. The list shows an empty state cleanly rather than crashing.

**7. REVIEW**
You open the diff. Two files changed: the list page and its stylesheet, exactly as scoped. No new dependencies. No stray edits. The new code follows the same component pattern as the rest of the page. You can explain, in one sentence per hunk, why every change is there. You approve it.

**8. LEARN**
Reflecting on the session, one small thing surprised you: the agent's first proposal had used a slightly different naming style for the filter buttons than the rest of the project's components. You caught it in review and asked for a rename. That is a rule worth capturing. You add one line to `AGENTS.md`:

> *"Interactive elements (buttons, filters, toggles) should follow the naming pattern used in `src/components/`. Match existing conventions rather than inventing new ones."*

The next time you or anyone else adds a similar element, that lesson is already learned.

That is one small feature, shipped in an afternoon, without drama. Nothing about it required advanced engineering skill. It required a defined task, a little context, a look before a leap, explicit boundaries, small steps, honest verification, careful review, and one sentence of learning captured for next time.

Do this ten times, and you will not just have ten features. You will have a project — and a way of working — that gets easier every week instead of harder.

---
