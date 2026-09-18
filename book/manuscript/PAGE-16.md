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
