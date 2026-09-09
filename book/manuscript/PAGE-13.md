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
