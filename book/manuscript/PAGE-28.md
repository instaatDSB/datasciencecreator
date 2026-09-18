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
