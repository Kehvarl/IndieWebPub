# First Run Experience

This document describes the user experience, not implementation details.

---

## Launch

When the application starts:

- No project is loaded
- The main window is mostly empty
- The UI invites the user to open or drag a folder

The app does not assume intent.

---

## Opening a Folder

The user may:

- Drag a folder into the window
- Choose a folder using a file dialog

The app treats both actions identically.

---

## Folder Inspection

When a folder is opened:

1. The app scans for subfolders
2. It looks for `.txt` files within them
3. It builds an in-memory view of stories and chapters

No files are modified during this process.

---

## Uninitialized Folder

If the folder does not resemble a story project:

The app displays a message similar to:

> This folder doesn’t look like a story project yet.  
> Would you like to set it up?

The wording avoids blame or error language.

---

## Initialization

If the user agrees to initialize:

- The app creates expected subfolders (if missing)
- No prose files are created
- Existing files are left untouched

Initialization is optional.
The app can continue in a read-only mode if the user declines.

---

## First Preview

Once a chapter is selected:

- The app renders it using the default reader layout
- The preview matches exported output styling
- System light/dark mode is respected

---

## Editing Loop

The expected workflow is:

1. User edits text in an external editor
2. User switches back to the app
3. The app refreshes the preview

No background file watching is required.
Refresh occurs on application focus.

