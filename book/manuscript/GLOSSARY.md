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
