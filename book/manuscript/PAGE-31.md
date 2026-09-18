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
