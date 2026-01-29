# Export Contract

Export is a promise to the user.

This document defines what that promise includes — and what it does not.

---

## What Export Does

Export produces a static website containing:

- One HTML file per chapter
- Optional index pages
- Shared CSS
- Referenced assets

The result is suitable for upload to any static host.

---

## What Export Never Does

Export will never:

- Modify original text files
- Write back into the project folder
- Embed tracking, analytics, or scripts
- Phone home
- Require an account or login

---

## Output Characteristics

- HTML is semantic and readable
- CSS prioritizes legibility over visual flair
- Mobile-first layout
- Honors system light/dark mode

The output should be readable without JavaScript.

---

## Determinism

Given the same input files and settings:

- Exported output should be identical
- Order should not change unexpectedly
- Filenames should be predictable

---

## User Control

The user chooses:

- Where export files are written
- When export occurs

The app does not auto-export.

---

## Long-Term Compatibility

Exported files should remain readable:

- Without the app
- Without future versions
- Without proprietary tooling

The output is intentionally boring.

