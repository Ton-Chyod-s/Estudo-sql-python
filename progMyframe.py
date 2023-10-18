from main import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import BD_myframecg as bd
from asyncio import run
import os
from PyQt6.QtCore import QTimer

class Principal(Ui_MainWindow, QMainWindow):
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.frame_erro.hide()
        self.pushButton_inserir.clicked.connect(self.inserir_cliente)
        self.pushButton_procurar.clicked.connect(self.procurar_pessoa)
        self.pushButton_criarBD.clicked.connect(self.criar_bd)
        self.pushButton_formulario.clicked.connect(self.formulario)
        self.pushButton_planilha.clicked.connect(self.planilha)
        self.pushButton_dashboard.clicked.connect(self.dashboard)
        self.pushButton_estoque.clicked.connect(self.estoque)
        self.pushButton_form_inserir.clicked.connect(self.inserir_estoque)
        self.pushButton_erro.clicked.connect(self.fechar_popup)

    def hide_message(self):
        self.frame_erro.hide()
        self.timer.stop()

    def inserir_cliente(self):
        def isEmpty(txt):
            if txt == '':
                txt = 'vazio'
            else:
                return txt
        caminho_bd = os.path.abspath('myframecg.db')  

        if os.path.exists(caminho_bd):    
            nome = isEmpty(self.lineEdit_nome.text())
            telefone = isEmpty(self.lineEdit_telefone.text())
            email = isEmpty(self.lineEdit_email.text())
            localidade = isEmpty(self.lineEdit_localidade.text())
            descricao = isEmpty(self.lineEdit_descricao.text())
            quantidade = isEmpty(self.lineEdit_quantidade.text())
            valor = isEmpty(self.lineEdit_valor.text())
            data = isEmpty(self.lineEdit_data.text())
            uberflash = isEmpty(self.lineEdit_uberflash.text())
            impressao = isEmpty(self.lineEdit_impressao.text())
            outros = isEmpty(self.lineEdit_outros.text())
            #inserindo informações no banco de dados
            run(bd.venda_realizada(nome,email,telefone,localidade,descricao,quantidade,valor,data,uberflash,impressao,outros))
            self.lineEdit_nome.setText('')
            self.lineEdit_telefone.setText('')
            self.lineEdit_email.setText('')
            self.lineEdit_localidade.setText('')
            self.lineEdit_descricao.setText('')
            self.lineEdit_quantidade.setText('')
            self.lineEdit_valor.setText('')
            self.lineEdit_data.setText('')
            self.lineEdit_uberflash.setText('')
            self.lineEdit_impressao.setText('')
            self.lineEdit_outros.setText('')

            self.label_erro.setText('Dados inserido com sucesso!')
            self.frame_erro.setStyleSheet("background-color: green;")
            self.frame_erro.show()
            # Configurar um timer para ocultar o rótulo após 1 segundo
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.hide_message)
            self.timer.start(1500)  # 1000 ms = 1 segundo

        else:
            self.label_erro.setText('Não tem banco de dados')
            self.frame_erro.show() 
 
    def inserir_estoque(self):
        def isEmpty(txt):
            if txt == '':
                txt = 'vazio'
            else:
                return txt
            
        nome = isEmpty(self.lineEdit_form_nome.text())
        produto = isEmpty(self.lineEdit_form_produto.text())
        ecomerce = isEmpty(self.lineEdit_form_ecomerce.text())
        quantidade = isEmpty(self.lineEdit_form_quantidade.text())
        valor = isEmpty(self.lineEdit_form_valor.text())
        data = isEmpty(self.lineEdit_form_data.text())

        run(bd.estoque(nome,produto,quantidade,valor,data,ecomerce))

        self.lineEdit_form_nome.setText('')
        self.lineEdit_form_produto.setText('')
        self.lineEdit_form_ecomerce.setText('')
        self.lineEdit_form_quantidade.setText('')
        self.lineEdit_form_valor.setText('')
        self.lineEdit_form_data.setText('')

        self.label_erro.setText('Dados inserido com sucesso!')
        self.frame_erro.setStyleSheet("background-color: green;")
        self.frame_erro.show()
        # Configurar um timer para ocultar o rótulo após 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide_message)
        self.timer.start(1500)  # 1000 ms = 1 segundo

    

    def procurar_pessoa(self):
        procurar_nome = self.lineEdit_procurar.text()
        bd.buscar_pessoa(procurar_nome)
        self.label_erro.setText('None encontrado')
        self.frame_erro.show()

    def criar_bd(self):
        caminho_bd = os.path.abspath('myframecg.db')

        if os.path.exists(caminho_bd):
            self.label_erro.setText('ja existe um banco de dados!')
            self.frame_erro.show()
        else:
            run(bd.create_database())
            self.label_erro.setText('Banco de dados criado com sucesso!!')
            self.frame_erro.show()

    def formulario(self):
        self.stackedWidget.setCurrentWidget(self.formulario_page)
    def planilha(self):
        self.frame_erro.hide()
        self.stackedWidget.setCurrentWidget(self.planilha_page)
    def dashboard(self):
        self.frame_erro.hide()
        self.stackedWidget.setCurrentWidget(self.resumo_page)
    def estoque(self):
        self.frame_erro.hide()
        self.stackedWidget.setCurrentWidget(self.estoque_page)
    def fechar_popup(self):
        self.frame_erro.hide()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
