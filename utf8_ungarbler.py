import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel
from mainWindow import MainWindow

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # On instancie une fenêtre graphique et l'affiche.
    myWindow = MainWindow()
    myWindow.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())
