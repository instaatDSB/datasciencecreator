## PAGE 19 — SET EXPLICIT BOUNDARIES

Once you can see the blast radius, the next move is to make the boundaries of a task explicit — in writing, in the instruction itself. Not in your head. Not "the agent should know." In the actual sentences you send.

A good task instruction has two halves. The first says what the agent should do. The second says what the agent must not do. The second half is the one beginners almost always forget, and it is usually the more important of the two.

For the Student Job Tracker, adding a "status" field might look like this:

> **REAL-WORLD EXAMPLE**
> **Change:**
> - The Applications list component (`src/pages/applications/list.tsx`) and its styles.
> - The data function that reads applications from the database.
>
> **Do not change:**
> - Authentication or anything under `src/auth/`.
> - The database schema (no new columns, no renamed columns).
> - Any file inside `src/payments/` or `src/config/`.
> - Unrelated components, even to "clean them up."
> - The production configuration file.

Reading that, the agent has almost no room to wander. It knows the rectangle it is allowed to work inside, and it knows the walls it must not lean against.

Why does this improve reliability so much? Because agents, like human developers, tend to expand to fill the space they are given. Without stated boundaries, an agent working on the Applications list may notice the sign-in page nearby, decide the styles are inconsistent, and "improve" them. It may spot a slightly awkward function in a neighboring file and refactor it. It may observe that a config value looks outdated and update it. Each of these moves might be individually defensible. Together, they are how a small, safe task becomes a large, risky one.

Explicit boundaries also make review possible. When you know exactly which files should have changed, opening the diff becomes a quick check: did the agent touch anything outside the rectangle? If yes, that alone is a reason to reject the change, no matter how good the code looks.

> **TRY THIS**
> Add this sentence to almost every task: *"Do not modify anything outside the files listed above. If you believe another file needs to change to complete this task, stop and tell me — do not change it yourself."* That single sentence will prevent more damage than any prompt trick you will ever learn.

Boundaries are not distrust. They are the working conditions that let both you and the agent do good work at speed.

---
