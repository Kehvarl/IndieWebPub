# Indie Web Publisher
This is a management tool authors can use to package up stories and apply a 
simple, consistent style so they're ready to publish on the Indie Web, and
can be read on a wide variety of devices.


# Simplified Design
A small, cross-platform desktop app for writers who want to publish their stories as clean, mobile-friendly static web pages — without changing how they write.

No built-in editor.  
No markup languages.  
No cloud.  
Just folders, text files, preview, and export.

---

## What This Is

Story Site Generator helps you:

- Organize stories stored as plain `.txt` files
- Preview them using a reader-friendly web layout
- Export a static site you can upload anywhere (e.g. Neocities)

You write in your editor of choice.  
The app reads from disk and stays out of the way.

---

## What This Is *Not*

This is **not**:

- A word processor
- A Markdown editor
- A CMS
- A collaborative platform
- A cloud service

Your files stay yours.

---

## Basic Idea

A “project” is just a folder.

Stories are folders.  
Chapters are text files.  
Order comes from filenames.

Example:
My Stories/
├─ stories/
│ ├─ Escape from Saturn/
│ │ ├─ 01_The_Hatch.txt
│ │ └─ 02_Captain_Dyer.txt
│ └─ Another Story/
│ └─ 01_Intro.txt
└─ assets/

That’s it.

No metadata files are required to get started.

---

## How You Use It

1. Launch the app
2. Drag a folder into the window **or** choose one from a file dialog
3. The app scans for stories and chapters
4. Select a chapter to see a preview
5. Edit text in your favorite editor
6. Switch back to the app — the preview refreshes automatically
7. Export when ready

---

## Preview

- Uses the same HTML and CSS that will be exported
- Optimized for mobile reading
- Respects system light/dark mode
- Refreshes automatically when the app regains focus

No live background file watching.  
No fighting your editor’s autosave.

---

## Export

Export produces a static website:

- One HTML page per chapter
- Optional index pages
- Shared CSS and assets

The output is ready to upload to any static host.

Your original text files are never modified.

---

## Design Goals

- Writer-first
- Folder-based
- Predictable
- Quiet
- Cross-platform (Windows, macOS, Linux)

The app should feel more like a helpful tool than a system you have to learn.

---

## Non-Goals

These are explicitly out of scope:

- Rich text editing
- Custom markup languages
- User accounts or cloud sync
- Collaboration features

If you want those, this probably isn’t the right tool.

---

## Status

Early design and prototyping.

Feedback from writers is welcome.

