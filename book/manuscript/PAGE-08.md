## PAGE 08 — DEFINE THE JOB

Almost every disappointing session with an AI coding agent starts the same way: the instruction was vague, so the agent filled in the blanks. It had no choice. Ambiguity does not stop an agent — it just gives it room to invent.

Look at this one, which sounds fine until you read it twice:

> "Improve the dashboard."

Improve how? For whom? Which dashboard, if there is more than one? Faster, prettier, easier to read, more mobile-friendly, more accurate? Improve using what — a new library, a redesign, a rewrite? And what happens to everything that is already working on that page?

The agent doesn't know. So it decides. And whatever it decides is unlikely to match what was in your head.

A well-defined task answers four questions before any code is written.

**1. Objective — what are you actually trying to achieve?**
Not the code. The outcome. *"So the student can tell at a glance which applications are still active."*

**2. Scope — what is inside the job, and what is outside?**
Which pages, which features, which files. Especially: what should *not* change.

**3. Expected result — what will the reader (and you) see when it works?**
A new button, a new column, a filter, a redirect — describe the visible outcome, not the implementation.

**4. Constraints — what must stay true?**
Existing behavior that must not break. Styles that must be respected. Data that must not be lost. Libraries you don't want added.

Put those four together and the earlier instruction becomes something an agent can actually work with. Using the Student Job Tracker:

> **REAL-WORLD EXAMPLE**
> **Objective:** Help the student quickly see which of their job applications are still active versus closed.
> **Scope:** The Applications list page only. Do not touch the Companies page or the Interview Stages view.
> **Expected result:** Each application in the list shows a small colored status label (Active, Rejected, Offer, Withdrawn). At the top of the list, a filter lets the student show only Active applications.
> **Constraints:** Do not change the underlying data model. Do not add new dependencies. The existing "Add Application" button must still work exactly as before.

Notice what happened. The task got longer — and infinitely clearer. There is now almost no room for the agent to invent. There is also almost no room for *you* to be surprised, which is the real point. A defined task is not paperwork. It is a promise you make to your future self about what you actually asked for.

> **TRY THIS**
> Before sending an instruction, read it back and ask: *"If I gave this to a stranger and they took it literally, would I be happy with any answer that fit?"* If the answer is no, you have not defined the job yet.

---
