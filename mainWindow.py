
from PySide6.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QLabel
from PySide6 import QtGui
from PySide6.QtGui import QIcon, QGuiApplication

# from eventTextWidget import EventTextWidget;

class MainWindow(QMainWindow):
    # Le constructeur de la classe nous permet de changer quelques caractéristiques.
    def __init__(self):
        # Appel au constructeur parent (QMainWindow).
        QMainWindow.__init__(self)
        self.setWindowTitle("UTF-8 ungarbler")
        self.setWindowIcon(QIcon("icons/file.png"))
        self.resize(1024, 768)

        centralArea = QWidget()
        # centralArea.setStyleSheet("background: #419eee")
        self.setCentralWidget(centralArea)

        # input column
        self.textInputLabel = QLabel("UTF-8 Garbled text input", centralArea)
        self.textInputLabel.setGeometry(10, 10, 500, 15)

        self.textInput = QPlainTextEdit("", centralArea)
        self.textInput.setGeometry(10, 30, 500, 700)
        self.textInput.keyPressEvent = self.inputChanges
        # self.textInput.scroll = self.test

        # self.textInput.verticalScrollBar().wheelEvent = self.scrollEvent
        self.textInput.wheelEvent = self.scrollEvent

        # output column
        self.textOutputLabel = QLabel("Output", centralArea)
        self.textOutputLabel.setGeometry(515, 10, 500, 15)

        self.textOutput = QPlainTextEdit("", centralArea)
        self.textOutput.setGeometry(515, 30, 500, 700)

    def inputChanges(self, event):
        # handle text paste
        if event.matches(QtGui.QKeySequence.Paste):
            self.textInput.insertPlainText(QGuiApplication.clipboard().text())

        # handle text select all
        if event.matches(QtGui.QKeySequence.SelectAll):
            self.textInput.selectAll()

        if (event.text() is not ""):
            self.textInput.insertPlainText(event.text())

        self.textOutput.setPlainText(self.processText(self.textInput.toPlainText()))

    def scrollEvent(self, event):
        vsb=self.textInput.verticalScrollBar()
        yPosition = event.pixelDelta().y()

        if (yPosition > 0):
            vsb.setSliderPosition(vsb.sliderPosition() + vsb.singleStep())
        else:
            vsb.setSliderPosition(vsb.sliderPosition() - vsb.singleStep())

        # sync output textarea position
        self.textOutput.verticalScrollBar().setSliderPosition(vsb.sliderPosition())


    # replace garbled accents
    def processText(self, text: str) -> str:
        text = text.replace("Ã©", "é")
        text = text.replace("Ã«", "ë")
        text = text.replace("Ã¨", "è")
        text = text.replace("Ãª", "ê")

        text = text.replace("Ã¶", "ö")
        text = text.replace("Ã´", "ô")

        text = text.replace("Ã ", "à")
        text = text.replace("Ã¢", "â")
        text = text.replace("Ã¤", "ä")

        text = text.replace("Ã§", "ç")

        text = text.replace("Ã¯", "ï")
        text = text.replace("Ã®", "î") 

        text = text.replace("Ã¹", "ù")

        return text

