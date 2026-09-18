## PAGE 15 — FIND THE RIGHT PLACE

Every change you make lives somewhere. Part of working well with an agent is helping it — and yourself — figure out *where* before figuring out *what.*

First, a plain-English definition. A **codebase** is simply the collection of all the files that make up your project: the code, the styles, the configuration, the small helper files that glue everything together. When people say "search the codebase," they mean "look across all those files at once, not just the one you happen to have open."

Real projects are almost never a single file. Even a small app like the Student Job Tracker might have dozens: a page for the list of applications, a page for a single application, a form for adding one, a shared component for the status label, a file for talking to the database, a stylesheet, a configuration file, a test or two. A change to "how status works" could plausibly live in any of them. Often it lives in several.

Good agents, given a task, will do something like this before editing:

- **Search the codebase for related words.** *"Where does the word `status` already appear? Where is `application` defined? Where is the list of applications rendered?"* A search across all files finds the touchpoints in seconds.
- **Trace a feature end to end.** Start at the visible thing (a button, a page, a column on screen), then follow it backward through the code: what happens when the user clicks it? What function runs? What file does that function live in? What does it call next? Keep going until you reach the data.
- **Find related components.** Many features are made of small parts that talk to each other — a form, a list, a shared label. Changing one without noticing the others is how "small" changes become large surprises.
- **Understand dependencies between files.** Which files import from which? If you change the shape of the data in one place, who else was relying on the old shape? These are the invisible strings between files, and they are where accidental damage travels.

You do not need to run these searches yourself. You need to *ask* for them. A useful pre-edit instruction to an agent sounds like:

> *"Before proposing changes, find every file that references the Applications list or the status of an application. List them. For each, describe in one sentence what it does. Then tell me where you think the change should live and why."*

The answer to that one instruction is often the entire difference between a clean change and a messy one. You learn where the work belongs. The agent proves it understood the project. And you both discover the surprises — the second copy of the status logic, the shared label used in three places, the old test that will need updating — *before* any code moves.

> **KEY IDEA**
> The first question of any task is not *"what should the code look like?"* It is *"where does this change belong, and what else touches it?"* Answer that first, and the code almost writes itself. Skip it, and no amount of typing will save you.

---
