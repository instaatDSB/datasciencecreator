## PAGE 17 — EXECUTE IN SMALL STEPS

Once a task is defined, scoped, and understood, execution begins. This is the stage where most beginners hand the wheel entirely to the agent and hope. Don't. Execution is where your role shifts from planner to pilot — still not typing every line, but staying in the loop, one step at a time.

A healthy execution loop looks like this:

- **One logical change at a time.** Ask the agent to make a single, self-contained edit — not five. *"Add the `status` field to the data layer. Do not touch the UI yet. Stop when you're done."* A tight instruction produces a tight change, which produces a tight review.
- **Inspect the results before continuing.** Look at what changed. Open the app. Click the thing. Read the diff. If step one is wrong, do not build step two on top of it — you are now building on sand.
- **Avoid unnecessary refactoring.** Agents often tidy. They will rename variables, move helpers, and "improve" code that had nothing to do with your task. This is a hidden cost: a five-line change becomes a fifty-line change, half of which you didn't ask for and now have to review. Explicitly say: *"Change only what is needed for this task. Do not refactor unrelated code."*
- **Preserve working functionality.** The features that already work are worth more than the feature you are adding. State this out loud. *"The existing Add Application flow must continue to work exactly as it does today. If your change would alter its behavior, stop and tell me instead."*
- **Use existing project patterns.** If the project already has a way of doing things — how components are structured, how data is fetched, how styles are written — the new code should look like the old code. Consistency is not aesthetics; it is what makes a codebase understandable at a glance, months later, when you have forgotten everything about it.

Behind all of these is a single idea: **the agent's autonomy should be controlled, not unlimited.**

An agent left completely free will do a lot. Much of it will look impressive. Some of it will quietly damage your project in ways you cannot see until much later. An agent kept on a short leash — one step, inspect, next step, inspect — moves slightly slower per instruction and often dramatically faster overall, because nothing has to be untangled after the fact.

In the Student Job Tracker, the difference shows up like this. Left free: *"Add application status."* Fifteen minutes later, the schema has changed, the form has been redesigned, two new components exist, an unused old file has been deleted, and something in the sign-in flow is subtly different. Kept on a leash: the same feature, delivered in six small, reviewable pushes, each of which left the app working.

> **KEY IDEA**
> The agent proposes. You approve. Every meaningful change should pass through your attention at least once before it becomes permanent. The moment that stops being true, you have lost the plot — no matter how good the last few outputs looked.

Which raises the next question, and the subject of the next chapter: how do you actually *set* those boundaries — not just in your head, but in a way the agent will respect?

---
