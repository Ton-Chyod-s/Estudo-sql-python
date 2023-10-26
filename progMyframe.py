from main import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QWidget, QFrame, QLabel
import sys
import BD_myframecg as bd
from asyncio import run
import os
from PyQt6.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import tratamento_db_v2 as tr
import plotly.graph_objs as go
import plotly.offline as pyo
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow, QApplication

class Principal(Ui_MainWindow, QMainWindow):
    def __init__(self,parent = None) -> None:
        tratamento = tr.tratamento_db()
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
        self.pushButton_baixar.clicked.connect(self.baixar_excel)
        self.pushButton_atualizar.clicked.connect(self.atualizar_bd)


        #acessando a aba DRE
        tab_dre = self.tabWidget.findChild(QWidget,'tab_dre')
        layout = QVBoxLayout(self.tab_dre)
        plt.figure(figsize=(6, 4))
        canvas = FigureCanvas(plt.gcf())

     
        # Adicione o canvas ao layout da aba
        layout.addWidget(canvas)

        ####----adicionando grafico no frame----####
        self.frame_vendas_mes = self.stackedWidget.findChild(QFrame,'frame_vendas_mes')
        layout = QVBoxLayout(self.frame_vendas_mes)
        
        plt.figure(figsize=(3, 2))
        canvas = FigureCanvas(plt.gcf())
        
        #tratamento.vendas()
        #tratamento.grafico_barra()

        
        # Adicione o canvas ao layout da aba
        layout.addWidget(canvas)

        ####----adicionando dados no frame----####
        
        
        
        ####----adicionando grafico no frame----####
        frame_localidade_vendas = self.stackedWidget.findChild(QFrame,'frame_localidade_vendas')
        layout = QVBoxLayout(self.frame_localidade_vendas)
        plt.figure(figsize=(1, 1))
        canvas = FigureCanvas(plt.gcf())
        

        # Adicione o canvas ao layout da aba
        layout.addWidget(canvas)

        ####----adicionando grafico no frame----####
        frame_localidades_vendas_2 = self.stackedWidget.findChild(QFrame,'frame_localidades_vendas_2')
        layout = QVBoxLayout(self.frame_localidades_vendas_2)
        plt.figure(figsize=(1, 1))
        canvas = FigureCanvas(plt.gcf())
        

        # Adicione o canvas ao layout da aba
        layout.addWidget(canvas)

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
            status = isEmpty(self.lineEdit_status.text())

            #inserindo informações no banco de dados
            run(bd.venda_realizada(nome,email,telefone,localidade,descricao,quantidade,valor,data,uberflash,impressao,outros,status))
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
            self.lineEdit_status.setText('')

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
        pessoa = str(run(bd.buscar_pessoa(procurar_nome))).replace("[","").replace("]","").replace(",",":")
        self.pessoa_registro = pessoa.split(':')
        
        venda = str(run(bd.buscar_id_venda(self.pessoa_registro[1]))).replace("[","").replace("]","")
        self.venda_registro = venda.split('.')

        despesas_venda = str(run(bd.buscar_id_despesas(self.venda_registro[1]))).replace("[","").replace("]","")
        self.despesas_venda_registro = despesas_venda.split(':')

        self.lineEdit_nome.setText(self.pessoa_registro[3])
        self.lineEdit_telefone.setText(self.pessoa_registro[7])
        self.lineEdit_email.setText(self.pessoa_registro[5])
        self.lineEdit_localidade.setText(self.pessoa_registro[9])
        self.lineEdit_descricao.setText(self.venda_registro[3])
        self.lineEdit_quantidade.setText(self.venda_registro[5])
        self.lineEdit_valor.setText(self.venda_registro[7])
        self.lineEdit_data.setText(self.venda_registro[9])
        self.lineEdit_uberflash.setText(self.despesas_venda_registro[1])
        self.lineEdit_impressao.setText(self.despesas_venda_registro[3])
        self.lineEdit_outros.setText(self.despesas_venda_registro[5])
        self.lineEdit_status.setText(self.venda_registro[13])
        
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
    
    def grafico (self):
        bd.grafico()

    def baixar_excel(self):
        tratamento = tr.tratamento_db()
        tratamento.planilha_completa()
        tratamento.salvar('Planilha BD.xlsx',)

        self.label_erro.setText('Planilha gerada com sucesso!')
        self.frame_erro.setStyleSheet("background-color: green;")
        self.frame_erro.show()
        # Configurar um timer para ocultar o rótulo após 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide_message)
        self.timer.start(1500)  # 1000 ms = 1 segundo
        
    def atualizar_bd(self):
        nome_novo = self.lineEdit_nome.text()
        telefone_novo = self.lineEdit_telefone.text()
        email_novo = self.lineEdit_email.text()
        localidade_novo = self.lineEdit_localidade.text()
        descricao_novo = self.lineEdit_descricao.text()
        quantidade_novo = self.lineEdit_quantidade.text()
        valor_novo = self.lineEdit_valor.text()
        data_novo = self.lineEdit_data.text()
        uber_novo = self.lineEdit_uberflash.text()
        impressao_novo = self.lineEdit_impressao.text()
        outros_novo = self.lineEdit_outros.text()
        status_novo = self.lineEdit_status.text()

        run(bd.atualizar_cliente_nome(self.pessoa_registro[3],nome_novo))
        run(bd.atualizar_cliente_whats_app(self.pessoa_registro[7],telefone_novo))
        run(bd.atualizar_cliente_e_mail(self.pessoa_registro[5],email_novo))
        run(bd.atualizar_cliente_localidade(self.pessoa_registro[9],localidade_novo))
        run(bd.atualizar_venda_produto(self.venda_registro[3],descricao_novo))
        run(bd.atualizar_venda_qtde(self.venda_registro[5],quantidade_novo))
        run(bd.atualizar_venda_valor(self.venda_registro[7],valor_novo))
        run(bd.atualizar_venda_data_pedido(self.venda_registro[9],data_novo))
        run(bd.atualizar_despesasvenda_uber_flash(self.despesas_venda_registro[1],uber_novo))
        run(bd.atualizar_despesasvenda_impressao(self.despesas_venda_registro[3],impressao_novo))
        run(bd.atualizar_despesasvenda_outros(self.despesas_venda_registro[5],outros_novo))
        run(bd.atualizar_venda_status(self.venda_registro[13],status_novo))

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
