from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox

class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.place = QLineEdit()
        self.date = QLineEdit()
        self.setWindowTitle('Beobachtungsbögen erstellen')
        btn_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow('Ort', self.place)
        layout.addRow('Datum', self.date)
        layout.addWidget(btn_box)

        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.rejected)

    def getInput(self):
        return self.place.text(), self.date.text()
