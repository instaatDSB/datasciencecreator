# THE AI CODING AGENT PLAYBOOK

*A beginner-friendly guide to working with AI coding agents — from your first instruction to a reliable development workflow.*

---

## PAGE 01 — COVER

**THE AI CODING AGENT PLAYBOOK**

*A beginner-friendly guide to working with AI coding agents — from your first instruction to a reliable development workflow.*

For students, career switchers, and new developers learning to build real software with AI.

---

## PAGE 02 — WHY DOES AI STILL BREAK THINGS?

Why can an AI coding agent write four hundred lines of code in ninety seconds — and still leave your project in worse shape than before you asked?

If you have spent any time with a modern AI coding tool, you have felt this moment. You typed a short request. The agent worked confidently. Files appeared. Code scrolled past. Something got installed. A message told you the task was complete.

Then you opened the app, and nothing worked.

Or worse: something that used to work now doesn't, and you can't tell what changed.

This is the strange paradox of the current moment. The tools are extraordinary. The results are unreliable. And most people quietly assume the problem is them — that they picked the wrong prompt, the wrong model, or the wrong tool.

It usually isn't any of those things.

The problem is almost never the prompt. The problem is almost always the environment the prompt was sent into: no clear task, no context, no boundaries, no way to verify the result, and no way to learn from what went wrong.

This book is about fixing that environment. Not with tricks. With a workflow.

---

## PAGE 03 — WHY THIS BOOK EXISTS

There are already thousands of articles about "the perfect prompt." There are prompt libraries, cheat sheets, and viral threads promising ten commands that will change your life.

They rarely change anything, because they treat the wrong layer of the problem.

**AI coding agents are genuinely powerful.** They can read a codebase, edit multiple files, run tests, install packages, follow instructions across several steps, and correct their own mistakes when guided well. Used carefully, a single person can now do work that used to require a small team.

**And yet beginners still struggle.** Not because the tools are bad, and not because beginners aren't smart. They struggle because nobody taught them the part that isn't the prompt.

Consider a familiar scene. You are building your first small project — let's call it a Student Job Tracker, an app to save companies you're applying to, track interview stages, and remember which follow-up email you owe on Thursday. You ask an AI agent to "add a way to mark an application as rejected." Ten minutes later, the agent has touched six files, renamed a column in your data, added a new button that doesn't appear anywhere, and broken the page that used to list your applications.

You did not write a bad prompt. You wrote a normal one. What was missing was everything around it: a clear definition of the task, the context the agent needed, the boundaries of what it should and shouldn't touch, and a way to check the result before it became a mess.

That surrounding structure is a workflow. This book teaches you one.

> **KEY IDEA**
> You don't get better results from AI coding agents by asking better questions. You get better results by giving the agent a better working environment.

If that idea sounds obvious, good. Most true things do, in hindsight. The rest of this book is about what "a better working environment" actually looks like, one concrete habit at a time.

---

## PAGE 04 — WHAT IS AN AI CODING AGENT?

Before going further, it helps to be precise about what an AI coding agent actually is — because the term gets used loosely, and the differences matter.

Three things often get grouped together. They are not the same.

**A chatbot** answers questions. You type; it replies. It lives inside a conversation window. It cannot open your files, run anything on your computer, or check whether its answer was correct. If you ask it how to fix a bug, it will describe a fix. Applying that fix is entirely your job.

*Think of it as a knowledgeable friend on the phone. Helpful, but not in the room with you.*

**A coding assistant** helps you write code while you write it. It suggests the next line, completes a function, or rewrites a small block you've highlighted. It sees the file you're in, and often a little more. You are still the driver — it is sitting in the passenger seat, pointing at the road.

*Think of it as an autocomplete that studied computer science.*

**A coding agent** is a different kind of thing. It can read across a whole project, decide which files to open, edit several of them, run commands in a terminal, execute tests, read the results, notice a failure, and try again. You give it a goal; it takes actions to reach that goal. Between your instruction and the finished result, it may make dozens of small decisions on its own.

*Think of it as a junior developer you just hired, working on your machine, who has never met you or your project before, and who will do exactly what you tell them — including the things you didn't realize you were telling them.*

That last analogy is the one to hold on to. It explains almost every surprising thing an agent does.

The specific tool you use — Claude Code, Codex, Cursor, GitHub Copilot's agent mode, Gemini CLI, or something newer by the time you read this — matters less than understanding which of these three you are actually working with in any given moment. The techniques in this book apply across all of them, because they are about you, not the tool.

---

## PAGE 05 — CHATBOT VS CODING AGENT

The move from chatbot to agent is not a small upgrade. It is a change in kind. Comparing them side by side makes the shift, and its consequences, easy to see.

|                       | **Chatbot**                       | **Coding Assistant**                       | **Coding Agent**                                                              |
|-----------------------|-----------------------------------|--------------------------------------------|-------------------------------------------------------------------------------|
| What it produces      | Words                             | Code suggestions inside a file             | Actual changes to your project                                                |
| What it can see       | Your message                      | The current file, sometimes a few nearby   | As much of your codebase as you allow, and as its context window permits      |
| What it can do alone  | Nothing                           | Insert or replace code you accept          | Read files, edit files, run commands, run tests, install packages, iterate    |
| Where the risk lives  | In whether you believe the answer | In whether you accept the suggestion       | In everything it does between your instruction and "done"                     |
| Your role             | Ask and evaluate                  | Write with help                            | Direct, constrain, and verify                                                 |

Notice how the last row changes. With a chatbot, your job is to think. With an assistant, your job is to write, with a smarter keyboard. With an agent, your job becomes something new: you are the person deciding what the agent should attempt, what it is allowed to touch, and whether the result is actually good.

That role has a name in every other field that uses it. A director on a film set does not operate the camera. A head chef does not plate every dish. What they do is set the intent, provide the context, mark the boundaries, and check the work. When any of those four things is missing, the output suffers — no matter how talented the crew.

Working with an AI coding agent is the same craft. And this is where the Student Job Tracker will keep returning throughout the book. Every technique — how to define a task, how to hand over context, how to keep the agent from wandering, how to verify what it built — will be shown against that one small, familiar project, so the ideas stay concrete instead of abstract.

> **REMEMBER**
> The more an AI system can do on its own, the more your workflow matters. A chatbot forgives a vague question. An agent does not — it acts on it.

That is why this book exists, and why the next pages start not with prompts, but with the first real habit of working with agents: learning to *define* the task before a single instruction is sent.

---

## PAGE 06 — THE BIG SHIFT

Somewhere between your first week and your third with an AI coding agent, a quiet shift has to happen. Most people never make it, and that is the difference between the users who eventually ship real projects and the ones who quietly go back to copy-pasting snippets from a chatbot.

The shift is this.

**Old thinking:** *Tell the AI what code to write.*
**New thinking:** *Give the AI a well-defined job inside a controlled environment.*

The old thinking treats the agent like a very fast typist. You describe the code you want; it produces it. If the result is wrong, you assume you described it badly, so you describe it again — longer, with more adjectives, maybe with an example. This is the "better prompt" trap. It can improve a small answer from a chatbot. It cannot save you from an agent that has quietly rewritten three files you didn't want touched.

The new thinking treats the agent like a capable stranger you just hired for the afternoon.

Imagine you hire a contractor to fix a leaking pipe under your kitchen sink. You do not hand them a hammer and say, "improve the kitchen." You show them the sink. You point at the leak. You tell them not to touch the dishwasher. You mention that the cabinet door is loose so they don't force it. You agree on what "done" looks like: no water on the floor, hot and cold both work, everything closes properly. Then you let them work.

The contractor is skilled. But the reason the job goes well is not their skill — it is the *frame* you built around the job before they picked up a wrench.

An AI coding agent needs the same frame. A defined job. A visible workspace. Known boundaries. A clear picture of success. Without these, even a highly capable agent will do highly capable damage, quickly, and with confidence.

This is the shift the rest of the book is built on. Everything from here forward is about how to build that frame, one piece at a time.

---

## PAGE 07 — THE AI CODING AGENT WORKFLOW

There are eight stages in a healthy workflow with an AI coding agent. You will not always do all of them in a strict order. But once you can name them, you can notice which one is missing when something goes wrong — and something going wrong is almost always a stage you skipped.

Here is the whole map, on one page. Each stage gets its own chapter later.

**1. DEFINE.** Turn a wish into a job. State the objective, the scope, and what "done" actually means, before the agent writes a single line.

**2. CONTEXT.** Give the agent the information a new teammate would need on day one: how the project is organized, what conventions it follows, and what it must not break.

**3. INVESTIGATE.** Before changing anything, have the agent (and yourself) understand the code that already exists. Most bad edits come from acting before looking.

**4. SET BOUNDARIES.** Say, in the instruction itself, which files and features the agent may touch — and which it may not. Explicit walls prevent quiet damage.

**5. EXECUTE.** Let the agent do the work — in controlled steps, not one giant leap. Small changes are easier to steer, easier to reverse, and easier to trust.

**6. VERIFY.** Prove that the change actually works. Open the app. Run the tests. Check the thing you asked for, and check the things you didn't ask about, because those are what quietly broke.

**7. REVIEW.** Read what the agent produced as if a coworker wrote it. Understand each change well enough to explain it. If you can't explain it, you don't yet own it.

**8. LEARN.** Notice the patterns. What tripped the agent up? What context was missing? Feed the answer back into your notes, your project documentation, and your next task — so the same mistake doesn't happen twice.

> **BEGINNER NOTE**
> Read the map once, then let it fade. You are not expected to memorize it. The point of naming the stages is so that later, when a task quietly falls apart, you can look at the wreckage and say, *"Ah — I skipped Investigate."* That is the entire skill.

The rest of Part One walks through the first three stages: **Define, Context, and Investigate.** These are the stages beginners skip most often, and the ones that pay back the most when done well. Part Two covers boundaries, execution, and verification. Part Three closes the loop: review and learning.

---

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

## PAGE 09 — DEFINE WHAT "DONE" MEANS

Defining the job tells the agent what to do. Defining "done" tells the agent — and yourself — when to stop.

This sounds like the same thing. It isn't.

An agent will happily tell you a task is complete the moment it finishes typing. That is not the same as the task actually being complete. "Complete" means the change works, the surrounding features still work, and the result matches what you asked for on a real screen, with real data, in the browser or app where the user will see it.

Without a written definition of done, every task drifts into a soft, agreeable ending. The agent says "Done!" You nod. You move on. Two hours later something is broken and neither of you can remember what changed.

A good definition of done is boring, specific, and checkable. You should be able to run through it like a short checklist and tick each line honestly.

For the Applications-status task from the previous page, "done" might look like this:

> **REAL-WORLD EXAMPLE**
> **Done means:**
> - The Applications list page loads without errors.
> - Every application row shows a colored status label.
> - Clicking the status filter narrows the list correctly, including "show all."
> - The existing "Add Application" button still opens the form and saves a new entry.
> - Nothing on the Companies page or Interview Stages page has changed.
> - The layout still looks correct on a phone-sized screen.
> - The project's existing tests still pass.

Notice what this list quietly does. It protects the parts of the app you didn't ask the agent to touch. Those are the parts most likely to break — not the feature under the spotlight, but the neighbors of that feature. A definition of done makes the neighbors visible.

Some of these checks you will do by hand (opening the page, clicking the button). Some the agent can do for you (running the tests). Later chapters will go deeper on both. For now, the habit is the point.

> **KEY IDEA**
> A task without a definition of done is an unfinished conversation. It ends whenever someone gets tired, not when the work is actually complete. Writing "done means…" in three or four lines, before the agent starts, is one of the highest-leverage habits in this entire book.

If you do only two things differently after reading this chapter — define the job, and define what "done" means — you will already be working with agents more skillfully than most people ever will.

---

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

## PAGE 11 — CONTEXT: AI NEEDS A MAP

Even the most carefully defined task will fall apart if the agent has no idea what kind of project it just walked into.

Imagine hiring that same contractor from the earlier analogy — clear job, clear scope, clear definition of done — and then dropping them in front of a house they have never seen, with no floor plan, no idea where the water shutoff is, no notes about which walls are load-bearing, and no clue that the electrical panel is behind the laundry room door. They are still skilled. They are also, now, guessing.

That is what happens to an AI coding agent when you give it a good instruction inside a project it doesn't understand. It will still act confidently. It will just be guessing.

**Context is the floor plan.** It is everything the agent needs to know to make good decisions inside your specific project, as opposed to some average project it has seen versions of during training.

Useful context for a project like the Student Job Tracker includes things like:

- **Project structure** — where the pages live, where shared components live, where the data layer sits. (*"Pages are in `src/pages/`. Reusable components in `src/components/`. Data access in `src/lib/db.ts`."*)
- **Architecture** — the shape of the thing. (*"This is a small web app with a single database. There is no separate backend service."*)
- **Coding conventions** — the local dialect. (*"We use functional components. We prefer named exports. Styles live next to the component in a `.module.css` file."*)
- **Commands** — how to actually run and test the project. (*"`npm run dev` starts the app. `npm test` runs the tests. `npm run build` must succeed before anything ships."*)
- **Testing instructions** — how you know something works. (*"Manual check: open `/applications`, add a fake application, refresh the page, confirm it persists."*)
- **Important constraints** — the load-bearing walls. (*"Never modify `src/auth/`. Never change the database schema without an accompanying migration file."*)
- **Existing patterns** — the way things are done here. (*"New pages should copy the pattern in `applications/list.tsx`. Do not introduce a new state management library — we use React's built-in hooks."*)

Written down once, this becomes the project's memory — a document the agent can read at the start of a task, so it does not have to guess who you are or how you like to work. Most modern AI coding tools have a conventional place for this: a file at the root of your project (often called something like `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or similar), which the tool reads before starting work. The exact filename matters less than the habit.

> **KEY IDEA**
> Most of what feels like "the AI got it wrong" is actually "the AI never had the information to get it right." Writing down your project's context is not busywork. It is the single most reusable piece of prompt engineering you will ever do — because you write it once, and every future task benefits.

In the next chapter, we will turn from *giving* context to *gathering* it — the Investigate stage, where the agent (and you) look before you leap.

---

## PAGE 12 — PROJECT MEMORY

Every time you open a new conversation with an AI coding agent, it starts from zero. It does not remember yesterday. It does not remember the last task. It does not remember the promise it made to never touch your authentication folder. Unless something reminds it, all of that context has to be reintroduced by you, by hand, every single time.

That is exhausting. It is also the reason many people quietly give up on agents after a few weeks. They mistake "I have to explain my project again" for "this tool doesn't work."

The fix is a very old idea in a new context: **write it down once, in a place the agent will always read.**

Most modern AI coding tools look for a specific file at the top of your project when a session starts. The exact name varies by tool, and the conventions will keep shifting. Common examples at the time of writing include:

- **`AGENTS.md`** — a growing shared convention across several agent tools.
- **`CLAUDE.md`** — used by Claude Code and some other Anthropic-facing tools.
- **`.cursorrules`** or **`.cursor/rules/`** — used by Cursor.
- **`README.md`** — the general-purpose project introduction that most tools (and every human) will read.
- **`docs/`** — a folder for longer explanations, architecture notes, and reference material.

Do not get attached to any one filename. They will change. The idea underneath will not. All of these files serve the same purpose:

> **KEY IDEA**
> A place where you store the instructions and knowledge you would otherwise have to repeat in every conversation.

Think of it as the project's memory. When a new agent session begins, that file is typically the first thing it reads — the equivalent of handing a new hire the onboarding document before their first meeting instead of explaining the company from scratch every morning.

For the Student Job Tracker, a short `AGENTS.md` might tell any agent, on any day:

- What the project is (*"a small web app for tracking student job applications"*).
- Where the important code lives (*"pages in `src/pages/`, shared components in `src/components/`, data in `src/lib/db.ts`"*).
- Which commands run and test the project.
- Which folders must not be modified without explicit permission.
- The one or two conventions the project cares about most.

That single file will save you hundreds of retyped sentences over the life of the project. More importantly, it will save you from the errors that happen when you *forget* to retype one of them.

> **REMEMBER**
> If you have explained the same thing to an agent twice, write it into project memory. If you have explained it three times, you should feel embarrassed that it isn't there already.

---

## PAGE 13 — WHAT SHOULD YOU DOCUMENT?

Project memory is only useful if it contains the right things. A bloated, contradictory, out-of-date file is worse than no file at all, because the agent will still read it and quietly follow instructions you no longer mean.

Aim for a short, honest document that answers the questions a competent new teammate would ask on their first day.

**Include:**

- **Architecture in one paragraph.** What is this project, in plain words? *"A single-page web app with a small local database. No separate backend. Deployed as static files."*
- **Important directories.** Where does each kind of thing live? Three or four lines is usually enough.
- **How to run and test it.** The actual commands. `npm run dev`, `npm test`, `npm run build`. If a command has a common gotcha (*"run `npm install` first if `node_modules/` is missing"*), name it.
- **Coding conventions that matter.** Not every stylistic preference — the ones that would produce visibly wrong-looking code if ignored. *"Use functional components. Named exports. Styles live in `.module.css` files beside the component."*
- **Testing expectations.** What counts as "tested" here? Automatic tests? A manual click-through? Both? Say so.
- **Deployment expectations.** Does anything happen automatically when code is pushed? Is there a staging environment? Anything the agent should never do on its own (like publishing a new version)?
- **Security-sensitive areas.** Authentication code, anything that touches user data, anything with API keys or environment variables. Name these folders explicitly and mark them off-limits without human approval.
- **Files or systems that require caution.** Database migrations, configuration files, anything a beginner would not think to be careful about. If there's a landmine, draw a circle around it.

**Leave out:**

- **Walls of generic advice** (*"write clean code," "use best practices"*). The agent already knows these phrases and cannot act on them.
- **Contradictory rules.** If two lines disagree, the agent will pick one — and it will not always be the one you meant.
- **Outdated instructions.** A rule about a folder that no longer exists is a trap for future agents. Delete it the moment it stops being true.
- **Long explanations of *why* the code exists.** Save those for a design document. Project memory is for *how to work here now.*

A useful test: read your own document out loud in under two minutes. If you can't, it is too long. If you can, and someone unfamiliar with the project could act on it, it is doing its job.

> **KEY IDEA**
> Useful documentation reduces uncertainty. Everything else is decoration. Every line that doesn't answer a question the agent will actually face is a line that dilutes the ones that do.

For the Student Job Tracker, the entire project memory might be less than a page. That is fine. Short and true beats long and aspirational, every time.

---

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

## PAGE 16 — MAKE THE SMALLEST SAFE CHANGE

There is a strong temptation, especially with an agent that can do so much so quickly, to hand over big tasks. *"Redesign the whole dashboard." "Refactor the data layer." "Rebuild the job tracker to look more like LinkedIn."*

Resist it. Not because agents can't attempt work at that size — they can — but because *you* can't safely review work at that size, and unreviewed work is not really finished work.

A small change is easier to:

- **Understand.** You can hold the whole thing in your head at once.
- **Test.** There are fewer things to click, fewer things that could have broken.
- **Review.** You can read the entire diff and know what it says.
- **Undo.** If something goes wrong, you throw away twenty minutes of work, not two days.
- **Debug.** When a bug appears, the list of suspects is short.

Every one of those advantages compounds. Large changes are not just a little riskier than small ones — they are catastrophically riskier, because the failure modes multiply with the surface area.

The professional habit here is called **incremental development.** It is the discipline of turning any big goal into a sequence of small, working, verifiable steps, and shipping each one before starting the next.

Compare these two versions of the same ambition.

**The tempting version:**
> *"Redesign the entire Student Job Tracker to feel more modern."*

That is one enormous, undefined task. If the agent's first attempt is 80% right, you now have to figure out which 20% is wrong across an entire redesigned app. Good luck.

**The disciplined version:**

1. Add a `status` field to applications, in the data layer only. Verify with a test.
2. Show the status as plain text on the list page. Verify by opening the page.
3. Replace the plain text with a colored label component. Verify visually.
4. Add a status filter to the top of the list. Verify by filtering.
5. Update the "Add Application" form so status can be set on creation. Verify by adding one.
6. Only now, revisit the visual design of the list as a whole.

Every step is small. Every step ends with a working app. If step 3 breaks something, you know exactly where to look, because steps 1 and 2 were fine ten minutes ago.

You have not moved more slowly. You have moved more *honestly.* And in practice, honest work is faster, because you never spend an afternoon trying to untangle a change you no longer understand.

> **REMEMBER**
> The size of a task is not measured by how ambitious it sounds. It is measured by how much can quietly break inside it. Aim for changes small enough that "quietly break" has almost nowhere to hide.

---

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

## PAGE 18 — UNDERSTAND THE BLAST RADIUS

We introduced the phrase "blast radius" briefly on Page 10, when we first talked about scope. Now it deserves a page of its own, because it is the single most useful lens you can bring to any change an agent proposes.

Blast radius is not about fear. It is about noticing, before you push a button, *how far a mistake could travel* if this change turns out to be wrong.

Some changes have almost no blast radius. Fixing a typo on a help page can only ever damage that help page. If it goes wrong, one line of text looks funny for ten minutes.

Other changes have a very large blast radius, even though they look small on the screen. Consider these examples, all of which have caught out beginners working with agents.

- **A change to one page quietly affects another.** In the Student Job Tracker, the "status label" component is used both on the Applications list and on the individual Application detail page. Redesigning it for the list page silently redesigns it on the detail page too — often not in the way you wanted.
- **A change to the database changes what every part of the app can see.** Rename a column and every page that read the old name goes blank. Rename it in the code and forget the database, and every save fails.
- **A change near authentication changes who can log in.** Even a small edit inside a login file — reordering two lines, "improving" a check — can lock existing users out of their account.
- **A change to a payment path can move real money.** Not relevant to a school project. Extremely relevant the day you get your first paying customer.
- **A change to how the app talks to an outside service (an API) can break the app for everyone at once,** the moment that service returns something slightly unexpected.
- **A change to existing user data is often permanent.** Deleting a column, transforming values in place, "cleaning up" old records — these actions can lose information that no backup will fully restore.

The point of this list is not to make you nervous. It is to teach you to *ask* one question before every task:

> **KEY IDEA**
> Before every change: *if this goes wrong, how much can it break, and how hard is it to undo?*

If the answer is "one page, and I can undo it in a click" — proceed cheerfully.
If the answer is "the whole app, and rolling back means restoring a backup I don't have" — stop, shrink the scope, and take a smaller step.

Measure the blast radius before the change, not after it. An agent will not do this for you. It is your job as the person in the room.

---

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

## PAGE 21 — THE FEEDBACK LOOP

There is a workflow shape that separates people who ship reliable software from people who ship confusing software. It looks like this:

**IMPLEMENT → TEST → FIX → TEST AGAIN → VALIDATE**

And there is another shape, the one beginners tend to use by default:

**IMPLEMENT → ASSUME IT WORKS**

The first shape is a loop. The second is a leap. Everything good about working with an AI coding agent depends on choosing the loop.

The loop is not complicated. It is only this: after every meaningful change, you (or the agent, under your direction) actually check that the change did what you meant it to. If it didn't, you fix it. Then you check again. When the checks pass — and only when they pass — you call it done.

For someone new to programming, the word "test" can sound formal, like something that requires special training. It doesn't. A test is anything that asks the software a question and gets back an honest answer. That question can be asked in different ways.

- **By a human.** You open the app, click the new button, and see whether the right thing happens. This is called *manual testing.* It is the oldest and most underrated form of verification.
- **By the computer, on your behalf.** You (or the agent) write a small piece of code whose only job is to check another piece of code. When you run it, it either says "passed" or "failed." This is called an *automated test.* It is not magic. It is a script that answers a specific question every time you run it.

Both count. Both are valid. What matters is that *some* honest check happens between "the agent finished typing" and "the task is done."

The loop earns its keep the moment something fails. Say you added the status filter to the Applications list, ran a manual check, and noticed that clicking "Rejected" also hides some applications that are clearly still active. Without the loop, you might not notice until a week later, by which point three more changes sit on top of the broken one and untangling them is a full afternoon. With the loop, you catch it now, describe the failure to the agent (*"clicking Rejected also hides applications where status is Offer"*), and fix it while everything is still fresh.

> **KEY IDEA**
> Treat "does it work?" as part of the task, not an afterthought. The task is not "add the filter." The task is "add the filter *and demonstrate that it works.*" Ending the loop early is not saving time. It is deferring the cost, usually with interest.

---

## PAGE 22 — WAYS TO CHECK THE WORK

There is no single way to verify that a change is correct. Serious projects use several, layered on top of each other, so that different kinds of mistakes are caught by different kinds of checks. You do not need to master all of them at once. You do need to know what each one is, and roughly what it protects against.

Here they are, in plain English.

**Automated tests.** Small pieces of code that check other pieces of code. You (or the agent) write them once; then they run in seconds, every time, forever. A good test for the Job Tracker might be: *"when I save an application with status Active and then read it back, its status is still Active."* If someone later breaks the save function, that test fails immediately.

**Linting.** A tool that reads your code and complains about small stylistic or structural problems — unused variables, inconsistent formatting, obvious mistakes like using a variable before defining it. Think of it as a spell-checker for code. It catches nothing about whether the software *does the right thing*, but it catches a lot of noise that would otherwise slow down review.

**Type checking.** In many modern projects, every piece of data has a declared shape — an application has an `id` (a number), a `company` (a string), a `status` (one of a fixed list of values). A type checker reads the whole project and complains if any piece of code tries to use data in a shape it isn't. If the agent adds a new status value and forgets to update the list of allowed statuses somewhere else, the type checker will catch many of these mismatches before you ever run the app.

**Build checks.** Before your app is deployed, it usually has to be *built* — packaged into the form that actually runs for users (a compact bundle of files that a web server or app store can hand out). A build check is simply: does that packaging succeed? A project that compiles fine while you are developing can still fail to build for release. Running the build after a change catches this.

**Manual testing.** You, using the app the way a real user would. Open the page. Click the button. Add an application. Filter by status. Refresh. Log out and back in. This is the check that most often catches the bugs no other tool will — the ones that live in the gap between "the code runs" and "the experience works."

**Checking expected behavior.** After a change, deliberately confirm that the specific thing you asked for actually happens. If the task was "show a colored status label on each row," open the list and look for colored labels on each row. It sounds trivial. It is skipped constantly.

**Checking edge cases.** After the normal path works, try the unusual ones. What happens with zero applications? A hundred? An application with a very long company name? An application with no status set? A user who is logged out? Edge cases are where the interesting failures live.

You will not run every check for every change. A one-line copy edit does not need a full test suite; a change to how applications are saved probably does. Match the depth of your verification to the blast radius of the change. Small changes, small checks. Large changes, layered checks.

---

## PAGE 23 — TESTS AS THE REFEREE

Of all the ways to check the work, automated tests deserve a page of their own — because they play a specific role that nothing else can play.

Tests are a **referee.** They are the piece of your project that gives an objective, repeatable answer to the question "does this still work?" — untouched by anyone's opinion or memory or hope.

That role matters more with AI coding agents than it ever did with humans alone, for a simple reason. Agents move fast and sound confident. When an agent tells you a change is complete, you have three options: trust the claim, spend time reviewing every line, or run a test that answers the question directly. Only the third scales.

Tests reduce guesswork. Without them, "does the save function still work?" is answered by *trying to remember* whether the last change might have affected it. With them, it is answered by running one command and reading one word: passed, or failed.

Tests increase confidence when they pass. If every test in the Job Tracker passes after the agent's change, you know — not hope — that all the behaviors those tests describe still work. You can move on to the next task with less anxiety, and less anxiety is not a soft benefit; it is what allows you to keep momentum without cutting corners.

But — and this is the part that is easy to miss — **passing tests are not proof of perfection.** They are only proof that the specific behaviors your tests describe still work. Anything your tests do not describe is still unknown territory. If you never wrote a test for what happens with an empty company name, a green test suite tells you nothing about that case. The referee only calls fouls on plays it can see.

This is why good tests are worth thinking about, not just producing. A useful test reflects a behavior you actually care about — something a real user would notice if it broke. *"Saving an application persists its status." "Filtering by Rejected shows only rejected applications." "The Add button opens the form."* A less useful test reflects incidental details of the code that could reasonably change tomorrow without anyone caring.

Ask the agent to write tests alongside changes, not as an afterthought. Ask for tests that describe *behavior* the user would notice, not internal wiring nobody outside the project cares about. And when a test fails, resist the temptation to "fix" it by making the test less strict. A failing test is the referee doing its job; silencing the referee is not the same as winning the game.

> **WATCH OUT**
> Tests are the most honest teammate on your project. They do not care how confident the agent sounded or how tired you are at 11 p.m. They only care whether the behavior they describe still holds. Treat them accordingly.

Even with strong tests, one form of verification remains irreplaceable: a human being reading the change, understanding it, and taking responsibility for it. That is the subject of the next chapter.

---

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

## PAGE 25 — THE HUMAN CHECKPOINT

A useful way to think about your role, once you have built a real workflow around an agent, is this: **the agent is allowed to be fast; you are required to be accountable.**

Speed and accountability are different jobs. Modern agents can absorb the speed job entirely. Nothing and nobody can absorb the accountability job for you. It is worth being specific about what that means in practice — what actually stays on your side of the line, no matter how capable the tools become.

**Product decisions.** What should this software do? Who is it for? Which features matter now, which can wait, and which are quietly bad ideas dressed up as reasonable requests? An agent can propose. It cannot decide, because deciding requires knowing what you and your users actually want, and the agent does not.

**Architecture decisions.** How the pieces of the project fit together. Whether this feature belongs in a new file or an existing one. Whether a small bit of duplication now is preferable to a premature abstraction. These decisions echo for months. They should be made by someone who will still be here in three months.

**Security.** Anything that touches authentication, user data, secrets, API keys, permissions, or the boundary between your project and the outside world. An agent following its default instincts will happily reduce friction in ways that also reduce safety. Every security-relevant change deserves a human looking at it slowly.

**Correctness.** In the end, someone has to be responsible for the claim "this works." Not "the agent said it works." Not "the tests passed." Someone has to have looked at the change, understood it, checked it, and stood behind it. That someone is you.

**Trade-offs.** Almost every real decision has costs on both sides — speed against clarity, flexibility against simplicity, features now against maintenance later. Agents are poor judges of trade-offs because they do not carry the consequences. You do.

**Final approval.** The moment where a change stops being a proposal and becomes part of the project. This should always be a human moment. Not an automatic one. Not a "sure, ship it" reflex. A pause, however short, in which you say, *"yes — I approve this, and I understand it."*

None of this means treating the agent as a suspect. It means treating yourself as the pilot. The agent can fly most of the plane most of the time. There is still a person in the seat, watching the instruments, making the calls at the moments that matter.

> **KEY IDEA**
> An AI coding agent can accelerate implementation. It should not silently own the decision-making. Anything that would embarrass a serious engineer to delegate to a junior on day one is not a good candidate for silent delegation to an agent either.

---

## PAGE 26 — TURN MISTAKES INTO RULES

Every time you work with an AI coding agent, something small goes wrong. The agent modifies a file it should not have. It invents a function name that doesn't exist. It picks a library you don't use. It "cleans up" code you liked the way it was. It over-refactors. It renames things without being asked.

Beginners react to each of these moments in isolation. They fix it, they sigh, they move on, and next week the same thing happens again. That is the trap.

Serious users of AI coding agents do something different, and it is the habit that eventually separates people who ship reliable software from people who chase the same bugs forever. They turn each recurring mistake into a **rule**, and they write the rule into a place the agent will read every time.

The loop is simple:

**MISTAKE → RULE → BETTER FUTURE BEHAVIOR**

You notice the mistake. You write a sentence that would have prevented it. You add that sentence to your project's memory — the `AGENTS.md`, `CLAUDE.md`, or equivalent file we talked about earlier. From that point on, every new session starts with that lesson already in place.

A few concrete examples, all drawn from the kinds of things beginners actually run into with a project like the Student Job Tracker.

> **REAL-WORLD EXAMPLE**
>
> **Problem:** The agent repeatedly modifies files outside the feature you asked about.
> **New rule:** *"Do not modify files outside the feature under discussion unless explicitly required. If you believe an outside file must change, stop and ask."*
>
> **Problem:** The agent keeps adding new libraries (external packages of pre-written code you install into a project) to solve small problems.
> **New rule:** *"Do not add new dependencies without explicit approval. Prefer solutions using the libraries already in `package.json`."*
>
> **Problem:** The agent quietly changes the database schema — the shape of the database, meaning which fields exist and what type each one is — when adding features.
> **New rule:** *"Never change the database schema in the same task as a UI change. Schema changes require their own task and their own review."*
>
> **Problem:** The agent writes tests only for the happy path.
> **New rule:** *"When adding a new feature, include at least one test for an edge case — empty input, missing field, or unexpected value."*
>
> **Problem:** The agent invents function names or files that don't exist.
> **New rule:** *"Before referring to a function or file, confirm it exists by searching the codebase. Do not assume."*

Each rule is short, specific, and written in the imperative. Each one closes a door that has been quietly slammed on you at least once. Together, over weeks and months, they turn your project memory from a generic onboarding document into something much more valuable: a record of the specific, hard-earned lessons this project has taught you.

> **TRY THIS**
> At the end of any session that produced a surprise, ask: *"What sentence, added to project memory, would have prevented this?"* Then add the sentence. That single question, asked honestly and often, is the difference between an agent that gets worse to work with over time and one that gets better.

---

## PAGE 27 — MAKE THE PROJECT BETTER AT WORKING WITH AI

There is a quiet, cumulative property to a well-run project that uses AI coding agents, and it is one of the most important ideas in this book. Stated plainly:

**A project should get easier to work with over time, not harder.**

Most codebases go the other direction. They start clean and small. Features pile on. Conventions drift. Documentation goes out of date. Nobody remembers why a particular file exists. Every new change costs more than the last, and every new person — human or agent — takes longer to become useful. This is entropy, and it happens by default.

Working carefully with an AI coding agent gives you an unusual opportunity to fight that entropy on purpose. Every session becomes a small chance to leave the project slightly better organized, slightly better explained, and slightly easier for the next task. Over months, the compound effect is dramatic.

Concretely, a well-tended project accumulates:

- **Clearer documentation.** Not more of it — clearer. The project memory sharpens with every rule you learn, every convention you decide is real, every landmine you draw a circle around.
- **Better tests.** Each new feature ships with tests for the behaviors that matter. Each bug you find becomes a test that will catch it if it ever returns. The referee gets stronger.
- **Stronger conventions.** *"This is how we do things here"* becomes an actual, written thing, not a vague feeling. Components look consistent. Files sit where you'd expect. New code fits into the shape of the old.
- **Better instructions.** Your task-writing improves. The kinds of tasks you send to the agent get sharper, more scoped, more defined. Fewer misfires. Fewer surprises.
- **Reusable workflows.** You start to recognize task shapes. *"Adding a new field to an existing entity"* becomes a familiar pattern, with a familiar checklist. So does *"adding a new page"* and *"changing an existing form."* The tenth time you do one of these is much cheaper than the first.
- **Fewer repeated mistakes.** The rules you wrote yesterday quietly prevent today's version of yesterday's problem. You stop stepping on the same rakes.

The paradox is that this makes the *agent* look better too — even though the agent hasn't changed. The same model, working inside a project with strong documentation, sharp conventions, and a well-tuned rules file, tends to produce dramatically better work than it does in a blank, chaotic one. What changed was not the intelligence in the machine. What changed was the environment you built around it.

That environment is portable in a deeper sense as well. Better documentation is better for the next human who joins the project. Better tests protect against every future change, human or otherwise. Better conventions make everything faster to read. In building a project that is friendly to AI agents, you have — almost as a side effect — built a project that is friendly to people.

> **KEY IDEA**
> Every task is two deliverables. One is the change itself. The other is a slightly better project to make the next change in. Beginners deliver only the first. Serious builders deliver both.

---

## PAGE 28 — THE COMPLETE AI CODING AGENT OPERATING SYSTEM

We started this book with a promise: that the difference between frustrating AI-assisted work and reliable AI-assisted work is not the prompt, but the workflow. It is now time to lay the full workflow out on one page, as an operating system rather than a list of tips.

Each stage exists to prevent a specific failure. Read the whole thing once. Come back to it whenever a task falls apart, and diagnose which stage you skipped.

**1. DEFINE.**
Turn a wish into a job. State the objective, the scope, the expected result, and what "done" means — in writing, before any code is written.
*Prevents: vague tasks that end whenever the agent gets tired.*

**2. CONTEXT.**
Give the agent the map it needs to work inside this specific project — structure, conventions, commands, and the parts of the system that require caution. Written once, in project memory, so it doesn't have to be retyped every session.
*Prevents: an agent guessing about your project instead of understanding it.*

**3. INVESTIGATE.**
Before changing anything, look. Have the agent read the relevant files, trace how the feature currently works, and report back. Only then propose the change.
*Prevents: building a second, parallel version of a system that already exists.*

**4. BOUNDARIES.**
Say, out loud, what the agent may and may not touch. Name the files that are inside the rectangle and the ones that are off-limits. Include the sentence *"If you believe another file must change, stop and ask."*
*Prevents: small tasks that quietly become large ones.*

**5. EXECUTE.**
Work in small, controlled steps. One logical change at a time. No unrequested refactoring. Reuse the project's existing patterns. Inspect the result before moving on.
*Prevents: unreviewable piles of "improvements" that all have to be untangled at once.*

**6. VERIFY.**
Prove the change works. Run the tests. Open the app. Check the specific thing you asked for. Check the neighboring features that were most likely to break. Try one or two edge cases.
*Prevents: shipping code that looks right and behaves wrong.*

**7. REVIEW.**
Read the diff. Understand every change. Confirm nothing outside the scope was touched. Take responsibility for the change as if you had written it yourself, because — as far as the project is concerned — you did.
*Prevents: silent damage hidden behind a green test suite.*

**8. LEARN.**
When something goes wrong, ask what rule, added to project memory, would have prevented it. Add the rule. Leave the project a little better organized than you found it.
*Prevents: making the same mistake a second time, and a third, and a fourth.*

That is the whole system. Eight stages, each defensible, each doing a specific job that no other stage can do. None of them are exotic. All of them are skippable, which is exactly why most beginners skip them.

> **THE INTELLECTUAL PAYOFF, IN ONE LINE**
> A prompt is one instruction. A workflow is the system that surrounds it. Good results come from good systems, not clever sentences.

If you finish this book remembering only that, and if you build even a rough version of this system into how you work, you will already be more effective with AI coding agents than most people who use them.

---

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

## PAGE 31 — THE TWO FINAL CHECKLISTS

You have the operating system. You have the template. This page collects the two shortest possible checklists — one for before you ask the agent to work, one for before you accept its work.

Use them the way a pilot uses a pre-flight checklist. Not because the pilot has forgotten how to fly, but because forgetting one small thing at speed is how accidents happen.

---

### Checklist 1 — BEFORE ASKING THE AGENT TO WORK

- [ ] I can state the **objective** of this task in one sentence.
- [ ] I have written **scope**: which files, pages, or features may change.
- [ ] I have written **boundaries**: what must not change, including any sensitive areas nearby.
- [ ] I have described the **expected result** in terms a user would recognize.
- [ ] I have named the **constraints** that must stay true (no new libraries, no schema changes, etc.).
- [ ] I have written a short, checkable **definition of done**.
- [ ] I have asked the agent to **investigate first** — read the relevant code and summarize it before editing.
- [ ] The instruction includes the standing rule: *"If you believe a file outside scope must change, stop and tell me."*
- [ ] The task is **small enough** that I can review the whole diff in one sitting. If not, I have split it.

---

### Checklist 2 — BEFORE ACCEPTING THE AGENT'S WORK

- [ ] I have **read the diff**, not skimmed it.
- [ ] Every changed file is either **expected** or has an **explanation I accept**.
- [ ] **No new dependencies** appeared that I did not approve.
- [ ] **Nothing outside the declared scope** was modified.
- [ ] The **tests still pass**, and any new behavior has at least one test covering it.
- [ ] I have **manually checked** the specific thing I asked for, on a real screen with real data.
- [ ] I have **spot-checked the neighbors** — the features most likely to break, even if I did not touch them.
- [ ] I have tried at least **one edge case** (empty, very large, missing, unexpected value).
- [ ] I can **explain each meaningful change** in one sentence, out loud.
- [ ] If anything surprised me, I have captured it as a **new rule** in project memory.

---

> **WATCH OUT — RED FLAGS THAT MEAN STOP**
> - The agent has touched files you did not name and cannot explain why.
> - The diff is too large to read in one sitting.
> - Tests were changed to "make them pass" instead of code being fixed.
> - A new library or dependency was added that you did not approve.
> - The database schema changed as a side effect of a UI task.
> - You are about to ship a change you do not understand because it's late and the tests are green.
>
> None of these are the end of the world. All of them are the moment where a small pause saves a large mess.

---

## PAGE 32 — THE FINAL PRINCIPLE

Tools change. Models change. The interface you use today will look old within a year, and the interface you use next year will look old the year after that. Whatever specific product name is on the tab in your browser right now — Claude Code, Cursor, Copilot, Codex, Gemini, something newer — will be joined, replaced, or subsumed by another.

Almost nothing in this book depended on which one you use.

What this book asked you to build is portable, because it lives in *you*, and in the small habits you leave behind in your projects. A short project-memory file. A task template you actually fill in. A definition of done that is checkable. A boundary line that says *stop and ask*. A diff you read before moving on. A rule captured after every surprise.

These are humble artifacts. None of them will trend on social media. Together, they are the difference between someone who is technically using AI and someone who is actually shipping.

Notice that none of them are prompts. The reason is now, hopefully, obvious.

**A prompt is a single instruction inside a single conversation.** Its lifespan is minutes. Its blast radius, at best, is one task.

**A workflow is a system that lives across every conversation you will ever have.** Its lifespan is the life of the project. Its blast radius, in the good sense, is every change you ever make.

If you get the workflow right, most bad prompts still produce acceptable results, because the environment around the prompt catches the mistakes. If you get the workflow wrong, no prompt is clever enough to save you, because the environment will keep producing the same class of failure no matter what you type.

The eight stages, one last time:

**DEFINE → CONTEXT → INVESTIGATE → BOUNDARIES → EXECUTE → VERIFY → REVIEW → LEARN**

And the single principle those eight stages exist to serve:

> **Don't aim for maximum AI autonomy. Aim for controlled autonomy.**

There is one more thing worth saying, at the end.

The reason to work this way is not just to write better code. It is to become the kind of person other people trust with real work. Not because you type faster than they do. Because when you say a change is done, it is actually done. Because when something breaks, you can explain why. Because you leave every project you touch a little easier for the next person to work in. That is a professional habit, not a technical one — and it will still be recognizable, decades from now, no matter what the tools look like then.

The playbook ends here. The practice starts on your next task.

Open the template. Define the job. Give the context. Investigate before editing. Set the boundaries. Execute in small steps. Verify honestly. Read the diff. Capture the lesson.

Then do it again.

That is how you become someone who works with AI coding agents well. And it is the only skill in this whole field that will still be worth having in ten years.

---

## GLOSSARY

Plain-English definitions of every technical term used in this book. If you meet a word here you didn't recognize in the text, you have not fallen behind — you have simply reached the page where it gets a definition.

**AI coding agent.** An AI system that can not only answer questions but take actions on your project: reading files, editing them, running commands, running tests, and iterating.

**API.** Short for *application programming interface.* The set of rules by which two pieces of software talk to each other. When your app fetches data from an outside service, it is calling that service's API.

**Architecture.** The overall shape of a project: what the main pieces are, how they connect, and where each kind of thing lives.

**Authentication.** The part of a system that decides *who a user is* (typically by checking a username and password, or a login token). Sensitive by nature.

**Authorization.** The part of a system that decides *what a user is allowed to do* once they have been identified. Related to authentication but not the same — one asks "who?", the other asks "may they?"

**Blast radius.** How much of a system can be damaged by a single change if that change goes wrong.

**Build.** The step that packages your project into the form that actually runs for users. A project that "compiles fine locally" can still fail to build.

**Chatbot.** An AI system that answers questions in a conversation window and cannot take actions on your computer or your project.

**Codebase.** The full set of files that make up a project.

**Coding assistant.** An AI system that helps you write code as you type, usually inside a single file. It suggests; you accept.

**Component.** A small, reusable piece of a user interface (like a button, a form field, or a status label) that can be dropped into different pages.

**Configuration.** Values that control how a project runs but are not part of the main code — things like which database to connect to, which environment to run in, or which keys to use.

**Constraint.** A rule about what must stay true during a change (e.g. *"existing behavior must not break," "no new dependencies"*).

**Convention.** A "the way we do things here" rule for a project — naming, structure, formatting. Not enforced by the machine, but by everyone who reads the code.

**Database.** The place your project stores information that must survive between sessions (like the list of job applications a student has saved).

**Definition of done.** A short, checkable list that describes what a completed task looks like. Prevents tasks from ending whenever the agent gets tired.

**Dependency (or library).** An external package of pre-written code that a project uses. Installing many dependencies makes a project heavier and harder to secure.

**Deployment.** The act of putting a version of your project in front of real users. Deployments are among the highest-blast-radius actions you can take.

**Diff.** A side-by-side view of what a change actually did — the exact lines removed and added.

**Edge case.** An input or situation that is unusual but legal — empty fields, very large numbers, missing values. Bugs love edge cases.

**Environment variable.** A configuration value stored outside your code, often used for secrets like API keys.

**Feedback loop.** The IMPLEMENT → TEST → FIX → TEST AGAIN → VALIDATE cycle. The alternative — IMPLEMENT → ASSUME — is where most silent failures come from.

**Framework.** A pre-built structure a project is built on top of (e.g. React, Next.js). Choosing one shapes almost everything about how the project is written.

**Function.** A named block of code that does a specific job.

**Git / GitHub.** Git is a system for tracking changes to code over time. GitHub is a popular website for hosting Git-tracked projects. Neither is required to use this book, but you will meet both eventually.

**Incremental development.** Turning a big goal into a sequence of small, working, verifiable steps.

**Integration test.** A test that checks whether two or more parts of a system work correctly together — a level up from a unit test.

**Investigate stage.** The part of the workflow where the agent reads and understands the code *before* changing it.

**Library.** See *dependency.*

**Linting.** A tool that flags small structural or stylistic mistakes in code — the "spell-checker for code."

**Manual testing.** You, opening the app and using it like a real user.

**Merge.** Combining a change into the main version of a project. Usually the point at which a change becomes "official."

**Migration (database migration).** A script that updates the shape of a database from one version to another. Sensitive; often irreversible.

**Payment path.** Any part of a system where money moves. Extremely high blast radius.

**Production.** The version of your project that real users actually see and use. As opposed to development or staging.

**Project memory.** A file (often `AGENTS.md`, `CLAUDE.md`, or similar) at the top of a project that describes how the project is organized and how the agent should behave. The agent reads it at the start of a session so you don't have to repeat yourself.

**Prompt.** A single instruction to an AI system.

**Refactor.** To rewrite code without changing what it does, usually to make it clearer or easier to extend. Useful in its place; dangerous when unrequested.

**Repository (or repo).** A single tracked project, often stored in Git.

**Schema.** The shape of a database — which fields exist, what types they are, and how they relate.

**Scope.** The set of files and features a task is allowed to touch.

**Test (automated).** A small piece of code whose only job is to check another piece of code. Runs quickly; answers *passed* or *failed*.

**Type checker.** A tool that reads a project and complains when a piece of code uses data in a shape that doesn't match its declared type.

**Unit test.** The smallest kind of automated test — one that checks a single function or component in isolation.

**Verify stage.** The step where you prove — not assume — that a change works.

**Workflow.** The complete system around a single instruction: defining the task, providing context, investigating, setting boundaries, executing, verifying, reviewing, and learning.

---

## FINAL REFERENCE CARD

*Tear this out. Keep it next to your keyboard. Or just remember it.*

---

**THE ONE-LINE THESIS**

*A prompt is one instruction. A workflow is the system around it. Good results come from good systems, not clever sentences.*

---

**THE EIGHT-STAGE OPERATING SYSTEM**

```
DEFINE
  ↓
CONTEXT
  ↓
INVESTIGATE
  ↓
BOUNDARIES
  ↓
EXECUTE
  ↓
VERIFY
  ↓
REVIEW
  ↓
LEARN
```

1. **DEFINE** — objective, scope, expected result, constraints, done.
2. **CONTEXT** — project memory: what this project is and how it works.
3. **INVESTIGATE** — read the code before changing it.
4. **BOUNDARIES** — what may change; what must not; *"stop and ask."*
5. **EXECUTE** — small steps; no unrequested refactoring; existing patterns.
6. **VERIFY** — the thing you asked for, the neighbors, tests, an edge case.
7. **REVIEW** — read the diff; explain every change; own it.
8. **LEARN** — turn each surprise into a rule; add it to project memory.

---

**THE FOUR QUESTIONS OF DEFINITION**

1. Objective — what outcome?
2. Scope — what's in, what's out?
3. Expected result — what will the user see?
4. Constraints — what must stay true?

---

**THE FIVE STEPS OF INVESTIGATION**

READ → TRACE → UNDERSTAND → PLAN → EDIT.

---

**THE STANDING RULE FOR EVERY TASK**

> *"Do not modify anything outside the files listed above. If you believe another file must change, stop and tell me — do not change it yourself."*

---

**THE FEEDBACK LOOP**

IMPLEMENT → TEST → FIX → TEST AGAIN → VALIDATE.

---

**THE SIX DIFF-REVIEW QUESTIONS**

1. What changed?
2. Why did it change?
3. Was anything unrelated modified?
4. Is it simpler than it needed to be?
5. Are there unexpected files?
6. Does it actually solve the original problem?

---

**RED FLAGS — STOP**

- Files outside scope were changed.
- The diff is too large to read in one sitting.
- Tests were softened instead of code being fixed.
- New dependencies appeared uninvited.
- The schema changed as a side effect.
- You cannot explain the change.
- You are about to ship late-at-night because "the tests passed."

---

**THE LEARNING LOOP**

MISTAKE → RULE → BETTER FUTURE BEHAVIOR.

*What one sentence, added to project memory, would have prevented this?*

---

**THE ATTITUDE**

The agent is allowed to be fast. **You are required to be accountable.**

---

**THE FINAL PRINCIPLE**

*Don't aim for maximum AI autonomy. Aim for controlled autonomy.*

---

*End of THE AI CODING AGENT PLAYBOOK.*
