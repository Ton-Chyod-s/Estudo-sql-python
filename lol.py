from custos_fixos import Ui_MainWindow_estoque
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QWidget, QFrame, QLabel
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

class Principal(Ui_MainWindow_estoque, QMainWindow):
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton_form_inserir.clicked.connect(self.inserir)


    def inserir(self):
        def isEmpty(txt):
            if txt == '':
                txt = 'vazio'
            else:
                return txt
            
        pro_labore = isEmpty(self.lineEdit_form_nome.text())
        ti = isEmpty(self.lineEdit_form_produto.text())
        site = isEmpty(self.lineEdit_form_ecomerce.text())
        dns = isEmpty(self.lineEdit_form_quantidade.text())
        marketing = isEmpty(self.lineEdit_form_valor.text())
        nuvem_arquivos = isEmpty(self.lineEdit_form_data.text())

        self.lineEdit_form_nome.setText('')
        self.lineEdit_form_produto.setText('')
        self.lineEdit_form_ecomerce.setText('')
        self.lineEdit_form_quantidade.setText('')
        self.lineEdit_form_valor.setText('')
        self.lineEdit_form_data.setText('')



qt = QApplication(sys.argv)
principal = Principal()
principal.show()
qt.exec()