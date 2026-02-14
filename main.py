import sys

from PyQt6.QtCore import Qt, QDir, QFileInfo
from PyQt6.QtGui import QAction, QFileSystemModel
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QTreeView, QWidget, QVBoxLayout, QStackedLayout, \
    QPushButton, QFileDialog


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setAcceptDrops(True)

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath("")

        self.treeview = QTreeView()
        self.treeview.setModel(self.dirModel)
        #self.treeview.setRootIndex(self.dirModel.index(QDir.homePath()))

        btnLoadProject = QPushButton("Load Project")
        btnLoadProject.clicked.connect(self.load_project)

        self.tree_stack = QStackedLayout()
        self.tree_stack.addWidget(btnLoadProject)
        self.tree_stack.addWidget(self.treeview)
        self.tree_stack.setCurrentIndex(0)

        stack_container = QWidget()
        stack_container.setLayout(self.tree_stack)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hello!"))
        layout.addWidget(stack_container)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def load_project(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Project Folder",
            QDir.homePath()
        )
        if path:
            self.load_project_path(path)

    def load_project_path(self, path):
        index = self.dirModel.index(path)
        if index.isValid():
            self.treeview.setRootIndex(index)
            self.tree_stack.setCurrentIndex(1)

    def set_root(self, path):
        index = self.dirModel.index(path)
        if index.isValid():
            self.treeview.setRootIndex(index)
            self.treeview.expandAll()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return

        info = QFileInfo(urls[0].toLocalFile())

        if info.isDir():
            path = info.absoluteFilePath()
        else:
            path = info.absolutePath()

        self.load_project_path(path)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()