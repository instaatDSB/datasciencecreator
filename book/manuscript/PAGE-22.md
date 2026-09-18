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
