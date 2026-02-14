import sys

from PyQt6.QtCore import Qt, QDir, QFileInfo
from PyQt6.QtGui import QAction, QFileSystemModel
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QTreeView, QWidget, QVBoxLayout, QStackedLayout, \
    QPushButton, QFileDialog


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IndieWeb Publish")
        self.setAcceptDrops(True)

        self.projectDirModel = QFileSystemModel()
        self.projectDirModel.setRootPath("")

        self.projectTreeView = QTreeView()
        self.projectTreeView.setModel(self.projectDirModel)
        self.projectTreeView.setRootIsDecorated(False)
        self.projectTreeView.setItemsExpandable(True)
        #self.treeview.setRootIndex(self.dirModel.index(QDir.homePath()))

        openProjectButton = QPushButton("Open Project")
        openProjectButton.clicked.connect(self.choose_project_folder)

        self.projectViewStack = QStackedLayout()
        self.projectViewStack.addWidget(openProjectButton)
        self.projectViewStack.addWidget(self.projectTreeView)
        self.projectViewStack.setCurrentIndex(0)

        stack_container = QWidget()
        stack_container.setLayout(self.projectViewStack)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hello!"))
        layout.addWidget(stack_container)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def choose_project_folder(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "Select Project Folder",
            QDir.homePath()
        )
        if path:
            self.open_project_root(path)

    def open_project_root(self, path):
        index = self.projectDirModel.index(path)
        if index.isValid():
            self.projectTreeView.setRootIndex(index)
            self.projectViewStack.setCurrentIndex(1)

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

        self.open_project_root(path)

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