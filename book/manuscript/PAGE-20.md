## PAGE 20 — CODE THAT LOOKS RIGHT CAN STILL BE WRONG

Here is a hard truth about working with AI coding agents, and one that takes most people a few painful sessions to fully absorb:

**Code that looks correct is not the same as code that works.**

An agent can produce a change that compiles cleanly, uses good names, follows the project's conventions, and reads like something a thoughtful senior engineer would write — and still be quietly, completely wrong. This is not a failure of the agent. It is a property of code in general. Software has always been able to look right and behave wrong. Agents just produce more of it, faster, which means the gap between "looks right" and "is right" now matters more than ever.

The gap has a few common shapes. It helps to be able to name them.

**Bugs.** The most familiar kind. The code does something, just not what you wanted. A filter that filters the wrong list. A save function that saves an empty record. A total that adds a number twice.

**Edge cases.** The code works for the normal path and fails for the unusual one. In the Student Job Tracker: adding an application with an empty company name crashes the list. Or a status filter works for four of the five status values and silently hides one.

**Integration problems.** Each piece works in isolation, but two pieces together do not. The new status label component looks fine on its own; dropped into the list page, it breaks the row layout on narrow screens. Or a new database function works when called directly, but the page that uses it never receives the result because the code that connects them was never updated.

**Side effects.** The change succeeds at what you asked for and accidentally changes something else. The new status filter works, and — because the agent quietly changed the sort order while it was in there — the list now shows the oldest applications first instead of the newest, and nobody noticed.

None of these failures show up when you skim the code. Some of them do not show up when you run the code, either. They show up the first time a real person uses the app in a way you didn't think to try.

The response to this is not to trust less. It is to *verify more*, in ways that are proportionate to the blast radius of the change. Every serious change should end not with "the agent said it was done" but with a visible answer to the question: **how do I actually know this works?**

That question is what the rest of this section is about.

---
