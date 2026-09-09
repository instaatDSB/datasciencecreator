## PAGE 14 — INVESTIGATE BEFORE EDITING

There is a temptation, when working with an AI coding agent, to skip straight to the edit. You have a task. The agent is fast. Why wait?

Because the fastest way to break a project is to change code you do not yet understand — and that is true whether the person changing it is you, a junior developer, or an agent working at a hundred lines per minute.

Before any change, healthy work moves through five steps:

**READ → TRACE → UNDERSTAND → PLAN → EDIT**

- **Read** the files that seem most related to the task. Not skim — read.
- **Trace** how those files connect. Where does the data come from? Where does it go? Who calls this function? What page uses this component?
- **Understand** what the current behavior actually is. Not what you *think* it is. What the code, right now, does.
- **Plan** the change in words before touching any code. Which files will change, in what order, and why.
- **Edit** — and only now — with the plan in hand.

Agents can and should do most of this for you. Modern coding agents are generally good at reading code, tracing references, and summarizing what a piece of the project actually does. Ask for that summary *before* you ask for a change:

> *"Before you modify anything, read the Applications list page and the file that saves application data. Summarize how a new application currently gets from the form to the database. Then propose a plan for adding a status field. Do not edit any files yet."*

Here is what happens when this step is skipped.

Back in the Student Job Tracker: you ask the agent to "add a Rejected status to applications." Without investigating, the agent invents a reasonable-sounding solution. It adds a new `status` field on the application form. It writes a new function to save it. It updates the list page to show it.

Then you try to add a rejected application, and the app crashes.

Why? Because the project already had a status system — a small one, half-built, in a file the agent never opened. The database column was already there under a different name. The list page was already reading from it. The agent didn't know, because it never looked. It built a second, parallel system on top of the first, and the two collided the moment you used them.

None of this would have happened if the first instruction had been: *before changing anything, look at how status is currently handled in this project and report back.* The agent would have found the existing pieces in seconds, and the task would have shrunk from "build a status system" to "finish the one that's already here."

> **WATCH OUT**
> Treat "look first" as the first stage of every task, not an optional detour. An agent that has read the code before editing it is a different, and much safer, agent than one that starts typing immediately.

---
