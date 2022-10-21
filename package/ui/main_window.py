from .q_drag_drop_list_widget import QDragDropListWidget
from .flow_layout import FlowLayout
from .toolbar import Toolbar
from .. import app
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QWidget, QScrollArea,
                             QStatusBar, QListWidgetItem)
import itertools

class MainWindow(QMainWindow):
    def __init__(self, icon_path):
        super().__init__()
        self.icon_path = icon_path
        self.setWindowTitle('TRP Gruppierer')
        self.toolbar = Toolbar(self, icon_path)
        self.addToolBar(self.toolbar)
        self.initLayout()

    def updateGroupNumLabel(self):
        self.toolbar.updateGroupNumLabel()

    def visualizeGroups(self, groups):
        self.clearLayout()
        self.list_widgets = []
        for group in groups:
            list_widget = QDragDropListWidget()
            self.list_widgets.append(list_widget)
            for fencer in group:
                list_widget.addItem(QListWidgetItem(str(fencer)))
            self.flayout.addWidget(list_widget)

    def getGroups(self):
        fencers = list(itertools.chain.from_iterable(app.groups))
        groups = []
        for list_widget in self.list_widgets:
            group = []
            for i in range(list_widget.count()):
                for fencer in fencers:
                    if list_widget.item(i).text() == str(fencer):
                        group.append(fencer)
                        break
            groups.append(group)
        return groups

    def clearLayout(self):
        for i in reversed(range(self.flayout.count())):
            self.flayout.itemAt(i).widget().setParent(None) # type: ignore

    def initLayout(self):
        self.flayout = FlowLayout()
        self.setMinimumSize(530, 665)
        widget = QWidget()
        widget.setLayout(self.flayout)
        vscroll = QScrollArea()
        vscroll.setWidgetResizable(True)
        vscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        vscroll.setWidget(widget)
        self.setCentralWidget(vscroll)
        self.setStatusBar(QStatusBar(self))
        self.setWindowIcon(QIcon(self.icon_path))
