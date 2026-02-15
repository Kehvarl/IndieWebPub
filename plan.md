ProjectManager Skeleton
- Create ProjectManager class
- Accept a folder path
- Scan subfolders for stories
- Scan .txt files for chapters
- Build in-memory structure: Story :: Chapter
- Expose stories list for UI consumption

Story/Chapter Data Classes 
- Define Story class
- Attributes: title, path, chapters
- Define Chapter class
- Attributes: filename, order, metadata (dict)

Tree View Refactor 
- Replace plain QFileSystemModel with QStandardItemModel
- Populate tree with stories and chapters from ProjectManager
- Add context menu placeholders:
- Add/Edit/Delete Story 
- Add/Edit/Delete Chapter

UI Layout Prep 
- Split stacked layout into:
- Left: Project Tree
- Right: Preview + Metadata placeholder
- Keep “Open Project” button for index 0 of stack

Drag-and-Drop / Folder Opening 
- Wire dropEvent to feed folder path into ProjectManager
- Update tree view after drop

Optional Quick Wins 
- Add print/log statements to verify scanning and tree population
- Add placeholder QTextBrowser for preview (empty for now)
- Add placeholder QLabel for metadata editing panel