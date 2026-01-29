# Mental Model

This application is a **filesystem reader and static site generator**.

It does not manage writing.
It does not own content.
It does not invent structure beyond what already exists on disk.

The filesystem *is* the source of truth.

---

## Core Concepts

### Project

A **project** is a folder chosen by the user.

The app never assumes ownership of the folder.
It only reads from it and writes output to a user-chosen export location.

A project may contain:
- Story folders
- Asset folders
- Nothing at all

There is no required metadata to be considered a valid project.

---

### Story

A **story** is a folder inside the project.

- The folder name is the story title by default
- Stories are discovered by scanning subfolders
- No registration step is required

The app does not care how many stories exist.
Single-story and multi-story projects are equally valid.

---

### Chapter

A **chapter** is a plain text file (`.txt`) inside a story folder.

- File order determines chapter order
- Filenames may include numeric prefixes for ordering
- File contents are treated as prose, not markup

The app does not modify chapter files.

---

### Assets

Assets are optional files (images, CSS overrides, etc.) that may be referenced by exported pages.

The app does not require assets to exist.

---

## Non-Concepts (Things the App Does Not Know About)

The app deliberately does not model:

- Characters
- Scenes
- Word counts
- Paragraph semantics
- Draft vs final states
- Writing progress

If it’s not representable by folders and files, it’s out of scope.

---

## Source of Truth

- Disk contents are authoritative
- The app does not cache prose
- Reloading always re-reads files

If the app and the filesystem disagree, the filesystem wins.

