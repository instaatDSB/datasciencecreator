## PAGE 24 — REVIEW THE DIFF

Before we can talk about reviewing a change, one piece of vocabulary is worth naming clearly: the **diff**.

A diff is simply a side-by-side view of what a change actually did. Not what the agent said it did. Not what you asked for. What the files, right now, look like compared to what they looked like a few minutes ago. Removed lines are shown in one color (usually red), added lines in another (usually green). Every serious code editor and every AI coding tool can show you one.

If tests are the referee, the diff is the game tape. It is where you find out what really happened.

Reading a diff is a skill you build slowly, and you do not need to understand every character of code to do it well. You only need to bring six questions with you.

- **What changed?** Which files were touched, and roughly what did each change do? If you cannot summarize this in one or two sentences, you have not yet read the diff carefully enough.
- **Why did it change?** For each meaningful edit, can you connect it back to the task you defined? If a change exists that you cannot explain in terms of the original task, that is a flag, not a feature.
- **Did the agent modify anything unrelated?** Look for edits outside the scope you set. A stray edit in a file you never mentioned is one of the most common sources of quiet damage.
- **Is the implementation simpler or more complicated than it needed to be?** Agents often solve small problems with impressively general solutions. A five-line change that does the job is almost always better than a fifty-line "framework" that does the same job plus four things you didn't ask for.
- **Are there unexpected files?** New files, deleted files, renamed files. Each one deserves a moment. Did you expect this file to exist? Do you understand what it is for?
- **Does the change actually solve the original problem?** Come back to the task definition and the definition of done. Do the words in the diff, read charitably, match the promise you made to yourself before starting?

None of these questions require you to be a strong programmer. They require you to be a careful reader who is willing to be honestly puzzled when something doesn't make sense — and to *ask*, out loud, until it does. *"Why did you add this new file?" "Why did you change the sort order here?"* A good agent will answer these questions clearly. A confused agent's answers will themselves be confused, which is useful information.

One warning worth stating plainly: **passing tests do not remove the need to read the diff.** Tests confirm that the behaviors you thought to test still work. The diff shows you everything else — the things you didn't test, the things you didn't ask for, the things that will surprise you a week from now. A green test suite plus an unread diff is one of the most dangerous combinations in AI-assisted development. It feels like safety. It isn't.

> **REMEMBER**
> Never merge, ship, or move on from a change you have not read. If the diff is too large to read in one sitting, that is the diff telling you the change was too large in the first place. Split it and try again.

---
