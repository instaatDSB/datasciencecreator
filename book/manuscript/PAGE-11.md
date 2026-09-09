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
