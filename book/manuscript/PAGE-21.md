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
