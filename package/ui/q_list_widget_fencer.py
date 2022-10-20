from PyQt6.QtWidgets import QListWidgetItem

class QListWidgetFencer(QListWidgetItem):
    def __init__(self, fencer):
        self.fencer = fencer
        super().__init__(str(fencer))
