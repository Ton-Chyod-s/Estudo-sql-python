from estoque import Ui_MainWindow_estoque
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QWidget, QFrame, QLabel
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

class Principal(Ui_MainWindow_estoque, QMainWindow):
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)


qt = QApplication(sys.argv)
principal = Principal()
principal.show()
qt.exec()