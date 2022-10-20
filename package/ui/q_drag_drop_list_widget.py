from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QListWidget

class QDragDropListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setDragEnabled(True)
        self.setDefaultDropAction(QtCore.Qt.DropAction.MoveAction)
        self.setWordWrap(True)
        self.setAcceptDrops(True)
        self.setFixedSize(250, 300)
        self.setAlternatingRowColors(True)
        self.model().rowsInserted.connect(self.update)
        self.model().rowsRemoved.connect(self.update)

    def update(self):
        self.setStatusTip(f'Teilnehmeranzahl in Gruppe: {self.count()}')
