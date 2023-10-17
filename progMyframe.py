from main import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import BD_myframecg as bd
from asyncio import run

class Principal(Ui_MainWindow, QMainWindow):
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        #self.frame_erro.hide()
        self.pushButton_inserir.clicked.connect(self.inserir_cliente)
        self.pushButton_criarBD.clicked.connect(self.criar_bd)
        self.pushButton_formulario.clicked.connect(self.formulario)
        self.pushButton_planilha.clicked.connect(self.planilha)
        self.pushButton_dashboard.clicked.connect(self.dashboard)
        self.pushButton_estoque.clicked.connect(self.estoque)


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

    

    def criar_bd(self):
        caminho_bd = '/myframecg.db'
        
        if caminho_bd != None:
            self.label_erro.setText('ja existe um banco de dados!')
        else:
            run(bd.create_database())
            self.label_erro.setText('Banco de dados criado com sucesso!!')

    def formulario(self):
        self.stackedWidget.setCurrentWidget(self.formulario_page)
    def planilha(self):
        self.stackedWidget.setCurrentWidget(self.planilha_page)
    def dashboard(self):
        self.stackedWidget.setCurrentWidget(self.resumo_page)
    def estoque(self):
        self.stackedWidget.setCurrentWidget(self.estoque_page)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
