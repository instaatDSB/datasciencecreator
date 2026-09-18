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
