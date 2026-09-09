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
