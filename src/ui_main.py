import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QTextEdit,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import QFont

import Social.visit_taverns as soc_tvrn
from Battle.battle import battle


class BattleWorker(QObject):
    finished = pyqtSignal()
    log = pyqtSignal(str)

    def run(self):

        self.log.emit('start tavern visitor')
        battle()
        self.finished.emit()


class TavernVisitWorker(QObject):
    finished = pyqtSignal()
    log = pyqtSignal(str)

    def run(self):

        self.log.emit('start tavern visitor')
        visitor = soc_tvrn.TavernVisitor()
        visitor.visitTaverns()
        self.finished.emit()


class FoeBotMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()

    def initUi(self):

        self.setWindowTitle('FoE bot control panel')
        widget = QWidget()
        vbLayout = QVBoxLayout()
        widget.setLayout(vbLayout)

        self.setCentralWidget(widget)

        textFont = QFont()
        textFont.setFamily('monospace [Consolas]')
        textFont.setFixedPitch(True)
        textFont.setStyleHint(QFont.Monospace)

        self.tedLog = QTextEdit(self)
        self.tedLog.setReadOnly(True)
        self.tedLog.setFont(textFont)
        self.tedLog.setText('Hello this is a test')
        self.tedLog.setMinimumSize(790, 590)

        self.btnTaverns = QPushButton(self)
        self.btnTaverns.setText('Visit taverns')
        self.btnTaverns.clicked.connect(self.onTavernsClicked)

        self.btnBattle = QPushButton(self)
        self.btnBattle.setText('Battle')
        self.btnBattle.clicked.connect(self.onBattleClicked)

        self.btnClearLog = QPushButton(self)
        self.btnClearLog.setText('Clear log')
        self.btnClearLog.clicked.connect(self.onClearLogClicked)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(self.btnTaverns)
        buttonsLayout.addWidget(self.btnBattle)

        vbLayout.addWidget(self.btnClearLog)
        vbLayout.addWidget(self.tedLog)
        vbLayout.addLayout(buttonsLayout)

    def setButtonsEnabled(self, value):
        self.btnTaverns.setEnabled(value)
        self.btnBattle.setEnabled(value)

    def onBattleClicked(self):
        # sender = self.sender()
        # self.tedLog.append('Button {} was pressed'.format(sender.text()))

        self.battleWorker = BattleWorker()
        self.battleWorkerThread = QThread()
        self.battleWorker.moveToThread(self.battleWorkerThread)

        self.battleWorkerThread.started.connect(self.battleWorker.run)
        self.battleWorker.finished.connect(self.battleWorkerThread.quit)
        self.battleWorker.finished.connect(self.battleWorker.deleteLater)
        self.battleWorkerThread.finished.connect(self.battleWorkerThread.deleteLater)

        self.battleWorker.log.connect(self.appendLog)

        self.battleWorkerThread.start()

        self.setButtonsEnabled(False)
        self.battleWorkerThread.finished.connect(lambda: self.setButtonsEnabled(True))
        self.battleWorkerThread.finished.connect(lambda: self.appendLog('battle completed'))

    def onTavernsClicked(self):
        # sender = self.sender()
        # self.tedLog.append('Button {} was pressed'.format(sender.text()))

        self.tavernWorker = TavernVisitWorker()
        self.tavernWorkerThread = QThread()
        self.tavernWorker.moveToThread(self.tavernWorkerThread)

        self.tavernWorkerThread.started.connect(self.tavernWorker.run)
        self.tavernWorker.finished.connect(self.tavernWorkerThread.quit)
        self.tavernWorker.finished.connect(self.tavernWorker.deleteLater)
        self.tavernWorkerThread.finished.connect(self.tavernWorkerThread.deleteLater)

        self.tavernWorker.log.connect(self.appendLog)

        self.tavernWorkerThread.start()

        self.setButtonsEnabled(False)
        self.tavernWorkerThread.finished.connect(lambda: self.setButtonsEnabled(True))
        self.tavernWorkerThread.finished.connect(lambda: self.appendLog('visit tavern completed'))

    def appendLog(self, text):
        self.tedLog.append(text)

    def onClearLogClicked(self):
        self.tedLog.clear()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)

    mainWindow = FoeBotMainWindow()
    mainWindow.resize(800, 600)
    mainWindow.show()

    sys.exit(qApp.exec())
