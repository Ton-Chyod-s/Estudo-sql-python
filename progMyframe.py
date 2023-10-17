from main import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

class Principal(Ui_MainWindow, QMainWindow):
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.frame_erro.hide()
        self.pushButton_inserir.clicked.connect(self.inserir_cliente)
        self.pushButton_formulario.clicked.connect(self.formulario)
        self.pushButton_planilha.clicked.connect(self.planilha)
        self.pushButton_dashboard.clicked.connect(self.dashboard)

    def inserir_cliente(self):
        nome = self.lineEdit_nome.text()
        telefone = self.lineEdit_telefone.text()
        email = self.lineEdit_email.text()
        localidade = self.lineEdit_localidade.text()
        descricao = self.lineEdit_descricao.text()
        quantidade = self.lineEdit_quantidade.text()
        valor = self.lineEdit_valor.text()
        data = self.lineEdit_data.text()
        uberflash = self.lineEdit_uberflash.text()
        impressao = self.lineEdit_impressao.text()
        outros = self.lineEdit_outros.text()

        print(f'{nome}, {telefone}, {email}, {localidade}, {descricao}, {quantidade}, {valor}, {data}, {uberflash}, {impressao}, {outros}')

    def formulario(self):
        self.stackedWidget.setCurrentWidget(self.formulario_page)
    def planilha(self):
        self.stackedWidget.setCurrentWidget(self.planilha_page)
    def dashboard(self):
        self.stackedWidget.setCurrentWidget(self.resumo_page)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
