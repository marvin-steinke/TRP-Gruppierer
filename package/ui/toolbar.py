from PyQt6.QtWidgets import QLabel, QToolBar, QFileDialog
from PyQt6.QtGui import QAction, QIcon
from .input_dialog import InputDialog
from .. import app

class Toolbar(QToolBar):
    def __init__(self, parent, icon_path):
        super().__init__()
        self.setWindowIcon(QIcon(icon_path))
        self.setMovable(False)
        self.parent = parent
        self.addBtnCSV()
        self.addSeparator()
        self.addBtnPDF()
        self.addSeparator()
        self.addSetGroupNum()
        self.addSeparator()
        self.addBtnRegroup()

    def addBtnRegroup(self):
        btn_regroup = QAction('Neu gruppieren', self)
        btn_regroup.setStatusTip('Gruppen neu einteilen')
        btn_regroup.triggered.connect(self.onBtnRegroup)
        self.addAction(btn_regroup)

    def onBtnRegroup(self):
        try:
            app.startGrouping()
        except:
            self.parent.statusBar().showMessage('Es liegt noch keine Datenquelle vor. Bitte wähle zuerst eine CSV-Datei.')
        else:
            self.parent.statusBar().showMessage('Die Teilnehmer wurden neu eingruppiert.')

    def addSetGroupNum(self):
        label = QLabel('Gruppenanzahl:', self)
        label.setStatusTip('Anzahl der Prüfenden festlegen')
        label.setStyleSheet('padding-left: 5px; padding-right: 3px')
        self.addWidget(label)
        btn_sub = QAction('-', self)
        btn_sub.triggered.connect(self.onBtnSub)
        self.addAction(btn_sub)
        self.group_num_label = QLabel(str(app.group_num), self)
        self.group_num_label.setStyleSheet('padding-left: 1px; padding-right: 1px')
        self.addWidget(self.group_num_label)
        btn_add = QAction('+', self)
        btn_add.triggered.connect(self.onBtnAdd)
        self.addAction(btn_add)

    def updateGroupNumLabel(self):
        self.group_num_label.setText(str(app.group_num))

    def onBtnAdd(self):
        app.group_num += 1
        self.updateGroupNumLabel()

    def onBtnSub(self):
        if app.group_num > app.weapons_num:
            app.group_num -= 1
            self.updateGroupNumLabel()

    def addBtnPDF(self):
        btn_pdf = QAction('Beobachtungsbögen erstellen', self)
        btn_pdf.setStatusTip('Gruppen in Beobachtungsbögen einfügen und als PDF speichern')
        btn_pdf.triggered.connect(self.onBtnPDF)
        self.addAction(btn_pdf)

    def onBtnPDF(self):
        if app.groups:
            dialog = InputDialog()
            if dialog.exec():
                place, date = dialog.getInput()
                doc = app.buildPDF(place, date)
                filepath = QFileDialog.getSaveFileName(self, 'Beobachtungsbögen speichern', f'Beobachtungsbögen TRP {date}.pdf')
                if filepath[0]:
                    doc.save(filepath[0])
                    self.parent.statusBar().showMessage(f'Beobachtungsbögen wurden erfolgreich unter {filepath[0]} abgespeichert.')
        else:
            self.parent.statusBar().showMessage('Es liegt noch keine Datenquelle vor. Bitte wähle zuerst eine CSV-Datei.')

    def addBtnCSV(self):
        btn_csv = QAction('CSV-Datei', self)
        btn_csv.setStatusTip('Teilnehmerliste aus ophardt.online im CSV Dateiformat auswählen')
        btn_csv.triggered.connect(self.onBtnChooseCSV)
        self.addAction(btn_csv)

    def onBtnChooseCSV(self):
        filepath = QFileDialog.getOpenFileName(self, 'Teilnehmerliste auswählen', filter='*.csv')
        if filepath[0]:
            self.parent.statusBar().showMessage(f'{filepath[0]} wurde als Datenquelle geladen und Teilnehmer wurden gruppiert.')
            app.startGrouping(filepath[0])
