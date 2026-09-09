## PAGE 18 — UNDERSTAND THE BLAST RADIUS

We introduced the phrase "blast radius" briefly on Page 10, when we first talked about scope. Now it deserves a page of its own, because it is the single most useful lens you can bring to any change an agent proposes.

Blast radius is not about fear. It is about noticing, before you push a button, *how far a mistake could travel* if this change turns out to be wrong.

Some changes have almost no blast radius. Fixing a typo on a help page can only ever damage that help page. If it goes wrong, one line of text looks funny for ten minutes.

Other changes have a very large blast radius, even though they look small on the screen. Consider these examples, all of which have caught out beginners working with agents.

- **A change to one page quietly affects another.** In the Student Job Tracker, the "status label" component is used both on the Applications list and on the individual Application detail page. Redesigning it for the list page silently redesigns it on the detail page too — often not in the way you wanted.
- **A change to the database changes what every part of the app can see.** Rename a column and every page that read the old name goes blank. Rename it in the code and forget the database, and every save fails.
- **A change near authentication changes who can log in.** Even a small edit inside a login file — reordering two lines, "improving" a check — can lock existing users out of their account.
- **A change to a payment path can move real money.** Not relevant to a school project. Extremely relevant the day you get your first paying customer.
- **A change to how the app talks to an outside service (an API) can break the app for everyone at once,** the moment that service returns something slightly unexpected.
- **A change to existing user data is often permanent.** Deleting a column, transforming values in place, "cleaning up" old records — these actions can lose information that no backup will fully restore.

The point of this list is not to make you nervous. It is to teach you to *ask* one question before every task:

> **KEY IDEA**
> Before every change: *if this goes wrong, how much can it break, and how hard is it to undo?*

If the answer is "one page, and I can undo it in a click" — proceed cheerfully.
If the answer is "the whole app, and rolling back means restoring a backup I don't have" — stop, shrink the scope, and take a smaller step.

Measure the blast radius before the change, not after it. An agent will not do this for you. It is your job as the person in the room.

---
