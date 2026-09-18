"""
Plain-language "In three lines" summaries shown at the top of every chapter.
Written so a total beginner can grasp the whole chapter in ten seconds.
"""

SUMMARIES = {
    "02": [
        "AI writes code fast, but often breaks things.",
        "It's usually not your prompt that's wrong.",
        "It's everything MISSING around the prompt.",
    ],
    "03": [
        "Better prompts don't fix bad results.",
        "A better SYSTEM around the prompt does.",
        "This book teaches that system, step by step.",
    ],
    "04": [
        "Chatbot = just talks.",
        "Assistant = suggests as you type.",
        "Agent = actually edits your project. Big difference.",
    ],
    "05": [
        "Agents can do a LOT more than chatbots.",
        "That's why they cause bigger surprises.",
        "The more powerful the tool, the more your rules matter.",
    ],
    "06": [
        "Stop thinking: 'tell AI what code to write.'",
        "Start thinking: 'give AI a clear job with clear limits.'",
        "Same as hiring a plumber — you point at the leak.",
    ],
    "07": [
        "There are 8 steps to a healthy AI task.",
        "This page shows all of them at once.",
        "Each one gets its own chapter next.",
    ],
    "08": [
        "'Improve the dashboard' is a bad instruction.",
        "Answer 4 questions first: what, where, result, rules.",
        "Then the agent has almost no room to guess wrong.",
    ],
    "09": [
        "'Done' isn't when the agent stops typing.",
        "It's when a real person could use it.",
        "Write a short checkable list — before you start.",
    ],
    "10": [
        "'Blast radius' = how much can break if this goes wrong.",
        "Small scope = small blast radius.",
        "Name what to touch. Name what to leave alone.",
    ],
    "11": [
        "The agent has never seen your project.",
        "Give it a map: folders, rules, commands.",
        "Save the map to a file. It reads it every time.",
    ],
    "12": [
        "'Project memory' is a file the agent reads first.",
        "Common names: AGENTS.md, CLAUDE.md.",
        "Write it once. Save yourself a hundred re-explanations.",
    ],
    "13": [
        "In project memory: architecture, folders, commands, rules.",
        "NOT: generic advice, contradictions, outdated lines.",
        "Keep it under two minutes to read.",
    ],
    "14": [
        "Bad idea: edit first, understand later.",
        "Good order: READ, TRACE, UNDERSTAND, PLAN, EDIT.",
        "Ask the agent to LOOK first. Every time.",
    ],
    "15": [
        "Before writing code, find where it belongs.",
        "Ask the agent to search the whole project.",
        "This one habit prevents most 'oops' moments.",
    ],
    "16": [
        "Big tasks fail in big ways.",
        "Small tasks are easy to test, review, and undo.",
        "Break every big goal into tiny working steps.",
    ],
    "17": [
        "One step. Look. Next step. Look.",
        "Say: 'don't refactor anything I didn't ask for.'",
        "You're the pilot. The agent flies while you watch.",
    ],
    "18": [
        "Some tiny changes reach into big places.",
        "Auth, database, payments = high blast radius.",
        "Before every task: 'if this goes wrong, how bad?'",
    ],
    "19": [
        "Every task has TWO halves: do this, do NOT do this.",
        "Most people skip the second half. That's the problem.",
        "One magic sentence: 'if you need to touch X, stop and ask.'",
    ],
    "20": [
        "Code that looks perfect can still be broken.",
        "Bugs, edge cases, side effects — none show at a glance.",
        "Never trust 'it looks right.' Actually test it.",
    ],
    "21": [
        "The loop: implement → test → fix → test → validate.",
        "A test is just asking the software 'does this work?'",
        "You can ask by hand or with code. Both count.",
    ],
    "22": [
        "Six ways to check the work — layer them.",
        "Manual clicks, tests, linting, types, builds, edge cases.",
        "Bigger change = more layers. Small change = fewer.",
    ],
    "23": [
        "Tests are the referee. They don't lie.",
        "Passing tests ≠ perfect. Only what YOU tested passes.",
        "Never soften a test to make it pass. Fix the code.",
    ],
    "24": [
        "A 'diff' shows exactly what changed. Red out, green in.",
        "Bring 6 questions when you read one.",
        "Never ship a change you didn't read.",
    ],
    "25": [
        "AI is fast. YOU are accountable.",
        "Product choices, security, final approval = yours.",
        "You are the pilot. Not the passenger.",
    ],
    "26": [
        "Every surprise = a new rule.",
        "Write the rule in project memory.",
        "Same mistake won't happen twice.",
    ],
    "27": [
        "A good project gets EASIER over time, not harder.",
        "Every session, leave better docs, tests, rules behind.",
        "Same AI + better project = way better results.",
    ],
    "28": [
        "The whole system on one page.",
        "8 stages. Each one prevents a specific failure.",
        "When a task fails, look here to spot which stage you skipped.",
    ],
    "29": [
        "One real task. All 8 stages. Start to finish.",
        "Watch how a vague wish becomes shipped code.",
        "This is what 'controlled autonomy' looks like in practice.",
    ],
    "30": [
        "A fill-in-the-blanks template you can steal today.",
        "Fill it before every task, until it's automatic.",
        "You're building your own operating manual.",
    ],
    "31": [
        "Two checklists: before you ask, and before you accept.",
        "Plus a list of RED FLAGS that mean 'stop.'",
        "Use them the way a pilot uses a pre-flight checklist.",
    ],
    "32": [
        "Tools will change. Your habits will not.",
        "The workflow is the only skill that compounds.",
        "Don't chase max autonomy. Aim for CONTROLLED autonomy.",
    ],
}
