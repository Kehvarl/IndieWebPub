import sys

from PyQt6.QtCore import Qt, QDir, QFileInfo
from PyQt6.QtGui import QAction, QFileSystemModel
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QTreeView, QWidget, QVBoxLayout


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setAcceptDrops(True)

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.homePath())

        self.treeview = QTreeView()
        self.treeview.setModel(self.dirModel)
        self.treeview.setRootIndex(self.dirModel.index(QDir.homePath()))


        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hello!"))
        layout.addWidget(self.treeview)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def set_root(self, path):
        index = self.dirModel.index(path)
        if index.isValid():
            self.treeview.setRootIndex(index)
            self.treeview.expandAll()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return

        info = QFileInfo(urls[0].toLocalFile())
        self.set_root(info.absoluteFilePath() if info.isDir() else info.absolutePath())

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