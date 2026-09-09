## PAGE 10 — SCOPE AND CONSTRAINTS

There is a phrase professional engineers use when they talk about risky changes: **blast radius.** It means, if this change goes wrong, how much of the surrounding world gets damaged?

A typo in a comment: blast radius of nothing.
Renaming a column in your database: blast radius of everything that ever read that column.

You do not need to become an engineer to use this idea. You just need to notice, before every task, how big the potential damage is — and then deliberately make it smaller. (We will return to blast radius on its own chapter later, once we have the vocabulary to talk about it in more depth.)

**Scope is how you shrink the blast radius on purpose.**

Think of your project as a house. Right now, you want to fix a squeaky door in the guest bedroom. You do not need — and do not want — the contractor rewiring the kitchen while they're at it, even if the kitchen wiring is a little old. A bigger job is not a better job. It is a job with more ways to fail, more things to test, and more surface area for surprises.

When you write a task for an AI agent, you are effectively defining the room they are allowed to work in. Be specific about three things:

**What the agent should change.**
Name the files, folders, pages, or features. *"Only the Applications list component and its associated styles."*

**What the agent should not change.**
Name the things that are near the work but off-limits. *"Do not modify the data model. Do not touch the Companies page. Do not add new libraries."*

**Which parts of the system are sensitive.**
Some areas of a project are load-bearing — authentication, payments, saved user data, anything to do with logins, keys, or configuration. Even if the current task is nowhere near them, it is worth naming them as untouchable. *"Do not modify anything under `/auth` or `/config`, even to improve it."*

For the Student Job Tracker, a scoped instruction might end with a line as simple as:

> Work only inside the Applications list feature. Do not modify the sign-in flow, the database schema, or any file outside the `applications/` folder.

That single sentence prevents an entire category of disaster. It costs you ten seconds to write. It can save you an evening of trying to figure out why you can no longer log in.

> **REMEMBER**
> If the blast radius of a task is bigger than you can comfortably review in one sitting, the task is too big. Split it. Ship the small version. Come back for the rest.

Small scopes are not timid. They are what allow you to move quickly *without* moving recklessly. The agent stays inside a room; you stay in control of the house.

---
