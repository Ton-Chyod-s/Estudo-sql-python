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
from PyQt6 import QtWidgets


class Principal(Ui_MainWindow, QMainWindow):
    def __init__(self,parent = None) -> None:
        self.tratamento = tr.tratamento_db()
        self.banco_dados = bd.estoque_()
        super().__init__(parent)
        super().setupUi(self)
        self.frame_erro.hide()
        self.pushButton_inserir_2.clicked.connect(self.inserir_cliente)
        self.pushButton_procurar_21.clicked.connect(self.procurar_pessoa)
        self.pushButton_criarBD_2.clicked.connect(self.criar_bd)
        self.pushButton_formulario.clicked.connect(self.formulario)
        self.pushButton_planilha.clicked.connect(self.planilha)
        self.pushButton_dashboard.clicked.connect(self.dashboard)
        self.pushButton_erro.clicked.connect(self.fechar_popup)
        self.pushButton_baixar.clicked.connect(self.baixar_excel)
        self.pushButton_atualizar_2.clicked.connect(self.atualizar_bd)
        self.pushButton_deletar_2.clicked.connect(self.deletar_linha_bd)
        self.pushButton_plan_atualizar.clicked.connect(self.atualizar)
        self.tableWidget_dre.setRowCount(22)
        self.tableWidget_planilha_cliente.setRowCount(150)
        self.tableWidget_planilha_estoque.setRowCount(50)
        self.pushButton_estoque_2.clicked.connect(self.estoque)
        self.pushButton_custo_fixo_2.clicked.connect(self.custos_fixos)
        self.planilha_venda()
        self.planilha_estoque()
        self.planilha_dre()

    def planilha_estoque(self):
        
        # Limpar a tabela (caso necessário)
        self.tableWidget_planilha_estoque.clearContents()

        tabela = self.tratamento.estoque_analise()
       
        def preencher_planilha(txt,coluna,linha):
                try:
                    # Adicionar um novo item à tabela
                    item = QtWidgets.QTableWidgetItem(txt)
                    self.tableWidget_planilha_estoque.setItem(linha, coluna, item)
                except Exception as e:
                    print(f"Erro ao preencher a linha {linha}: {str(e)}")
        cont = 0

        for linha in range(len(tabela)):
            fornecedor = tabela['Fornecedor'][linha]
            produto = tabela['Produto'][linha]
            quantidade = tabela['Quantidade'][linha]
            ecommerce = tabela['E-commerce'][linha]
            
            preencher_planilha(fornecedor,0,cont)
            preencher_planilha(produto,1,cont)
            preencher_planilha(quantidade,2,cont)
            preencher_planilha(ecommerce,3,cont)
        
            cont += 1

    def planilha_venda(self):
    
        # Limpar a tabela (caso necessário)
        self.tableWidget_planilha_cliente.clearContents()

        tabela = self.tratamento.planilha_completa()
       
        def preencher_planilha(txt,coluna,linha):
                try:
                    # Adicionar um novo item à tabela
                    item = QtWidgets.QTableWidgetItem(txt)
                    self.tableWidget_planilha_cliente.setItem(linha, coluna, item)
                except Exception as e:
                    print(f"Erro ao preencher a linha {linha}: {str(e)}")
        cont = 0
        for linha in range(len(tabela)):
            nome = tabela['nome'][cont]
            whats_app = tabela['whats-app'][cont]
            localidade = tabela['localidade'][cont]
            data_prazo = tabela['Data prazo'][cont]
            situacao = tabela['Situação'][cont]

            preencher_planilha(nome,0,cont)
            preencher_planilha(whats_app,1,cont)
            preencher_planilha(localidade,2,cont)
            preencher_planilha(data_prazo,3,cont)
            preencher_planilha(situacao,4,cont)

            cont += 1
    
    def planilha_dre(self):
        # Limpar a tabela (caso necessário)
        self.tableWidget_dre.clearContents()

        tabela = self.tratamento.dre()
       
        def preencher_planilha(txt,coluna,linha):
                try:
                    # Adicionar um novo item à tabela
                    item = QtWidgets.QTableWidgetItem(txt)
                    self.tableWidget_dre.setItem(linha, coluna, item)
                except Exception as e:
                    print(f"Erro ao preencher a linha {linha}: {str(e)}")

        def preencher_planilha_numero(txt,coluna,linha):
                try:
                    # Adicionar um novo item à tabela
                    item = QtWidgets.QTableWidgetItem(txt)
                    self.tableWidget_dre.setItem(linha, coluna, item)
                except Exception as e:
                    print(f"Erro ao preencher a linha {linha}: {str(e)}")

        cont = 0

        for linha in range(len(tabela)):
            dre = tabela["Descrição"][linha]
            janeiro = f'{tabela["Janeiro"][linha]:.2f}'
            fevereiro = f'{tabela["Fevereiro"][linha]:.2f}'
            marco = f'{tabela["Março"][linha]:.2f}'
            abril = f'{tabela["Abril"][linha]:.2f}'
            maio = f'{tabela["Maio"][linha]:.2f}'
            junho = f'{tabela["Junho"][linha]:.2f}'
            julho = f'{tabela["Julho"][linha]:.2f}'
            agosto = f'{tabela["Agosto"][linha]:.2f}'
            setembro = f'{tabela["Setembro"][linha]:.2f}'
            outubro = f'{tabela["Outubro"][linha]:.2f}'
            novembro = f'{tabela["Novembro"][linha]:.2f}'
            dezembro = f'{tabela["Dezembro"][linha]:.2f}'
            
            preencher_planilha(dre,0,cont)
            preencher_planilha_numero(f'{janeiro}',1,cont)
            preencher_planilha_numero(f'{fevereiro}',2,cont)
            preencher_planilha_numero(f'{marco}',3,cont)
            preencher_planilha_numero(f'{abril}',4,cont)
            preencher_planilha_numero(f'{maio}',5,cont)
            preencher_planilha_numero(f'{junho}',6,cont)
            preencher_planilha_numero(f'{julho}',7,cont)
            preencher_planilha_numero(f'{agosto}',8,cont)
            preencher_planilha_numero(f'{setembro}',9,cont)
            preencher_planilha_numero(f'{outubro}',10,cont)
            preencher_planilha_numero(f'{novembro}',11,cont)
            preencher_planilha_numero(f'{dezembro}',12,cont)

            cont += 1

    def atualizar(self):
        self.planilha_venda()
        self.planilha_estoque()
        self.planilha_dre()

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
        try:
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
                self.lineEdit_nome_2.setText('')
                self.lineEdit_telefone_2.setText('')
                self.lineEdit_email_2.setText('')
                self.lineEdit_localidade_2.setText('')
                self.lineEdit_descricao_3.setText('')
                self.lineEdit_quantidade_3.setText('')
                self.lineEdit_valor_3.setText('')
                self.lineEdit_data_3.setText('')
                self.lineEdit_uberflash_2.setText('')
                self.lineEdit_impressao_2.setText('')
                self.lineEdit_outros_2.setText('')
                self.lineEdit_status_2.setText('')

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
        except:
            self.label_erro.setText('Existe varios campos em branco, Revise!')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()
    
    def inserir_estoque(self):
        def isEmpty(txt):
            if txt == '':
                txt = 'vazio'
            else:
                return txt
            
        nome = isEmpty(self.lineEdit_form_nome.text())
        if nome == None:
            self.label_erro.setText('Campo em branco')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()
        else:    
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
        procurar_nome = self.lineEdit_procurar_2.text()
        try:
            pessoa = str(run(bd.buscar_pessoa(procurar_nome))).replace("[","").replace("]","").replace(",",":")
            self.pessoa_registro = pessoa.split(':')
        
            venda = str(run(bd.buscar_id_venda(self.pessoa_registro[1]))).replace("[","").replace("]","")
            self.venda_registro = venda.split(',')

            despesas_venda = str(run(bd.buscar_id_despesas(self.venda_registro[1]))).replace("[","").replace("]","")
            self.despesas_venda_registro = despesas_venda.split(':')

            self.lineEdit_nome_2.setText(self.pessoa_registro[3])
            self.lineEdit_telefone_2.setText(self.pessoa_registro[7])
            self.lineEdit_email_2.setText(self.pessoa_registro[5])
            self.lineEdit_localidade_2.setText(self.pessoa_registro[9])
            self.lineEdit_descricao_3.setText(self.venda_registro[3])
            self.lineEdit_quantidade_3.setText(self.venda_registro[5])
            self.lineEdit_valor_3.setText(self.venda_registro[7])
            self.lineEdit_data_3.setText(self.venda_registro[9])
            self.lineEdit_uberflash_2.setText(self.despesas_venda_registro[1])
            self.lineEdit_impressao_2.setText(self.despesas_venda_registro[3])
            self.lineEdit_outros_2.setText(self.despesas_venda_registro[5])
            self.lineEdit_status_2.setText(self.venda_registro[13])

        except:
            self.label_erro.setText('Cliente não encontrado no banco de dados!')
            self.frame_erro.setStyleSheet("background-color: red;")
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
        from estoque import Ui_MainWindow_estoque

        self.janela = QtWidgets.QMainWindow()
        self.estoque_ = Ui_MainWindow_estoque()
        self.estoque_.setupUi(self.janela)
        self.janela.show()
        qt.exec()
        #self.pushButton_form_inserir.clicked.connect(self.inserir_estoque)
        #self.pushButton_form_atualizar.clicked.connect(self.atualiza_estoque)
        #self.pushButton_form_deletar.clicked.connect(self.deletar_linha_estoque)
        #self.pushButton_form_procurar.clicked.connect(self.procurar_estoque)
    
    def custos_fixos(self):
        from custos_fixos import Ui_MainWindow_estoque

        self.janela = QtWidgets.QMainWindow()
        self.estoque_ = Ui_MainWindow_estoque()
        self.estoque_.setupUi(self.janela)
        self.janela.show()
        qt.exec()

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
        self.timer.start(2000)  # 2000 ms = 2 segundo
        
    def atualizar_bd(self):
        try:
            nome_novo = self.lineEdit_nome_2.text()
            telefone_novo = self.lineEdit_telefone_2.text()
            email_novo = self.lineEdit_email_2.text()
            localidade_novo = self.lineEdit_localidade_2.text()
            descricao_novo = self.lineEdit_descricao_3.text()
            quantidade_novo = self.lineEdit_quantidade_3.text()
            valor_novo = self.lineEdit_valor_3.text()
            data_novo = self.lineEdit_data_3.text()
            uber_novo = self.lineEdit_uberflash_2.text()
            impressao_novo = self.lineEdit_impressao_2.text()
            outros_novo = self.lineEdit_outros_2.text()
            status_novo = self.lineEdit_status_2.text()

            run(bd.atualizar_cliente_nome(self.pessoa_registro[3],nome_novo))
            run(bd.atualizar_cliente_whats_app(self.pessoa_registro[7],telefone_novo))
            run(bd.atualizar_cliente_e_mail(self.pessoa_registro[5],email_novo))
            run(bd.atualizar_cliente_localidade(self.pessoa_registro[1],localidade_novo))
            run(bd.atualizar_venda_produto(self.venda_registro[3],descricao_novo))
            run(bd.atualizar_venda_qtde(self.venda_registro[5],quantidade_novo))
            run(bd.atualizar_venda_valor(self.venda_registro[7],valor_novo))
            run(bd.atualizar_venda_data_pedido(self.venda_registro[9],data_novo))
            run(bd.atualizar_despesasvenda_uber_flash(self.venda_registro[1],uber_novo))
            run(bd.atualizar_despesasvenda_impressao(self.venda_registro[1],impressao_novo))
            run(bd.atualizar_despesasvenda_outros(self.venda_registro[1],outros_novo))
            run(bd.atualizar_venda_status(self.venda_registro[13],status_novo))

            self.lineEdit_nome_2.setText('')
            self.lineEdit_telefone_2.setText('')
            self.lineEdit_email_2.setText('')
            self.lineEdit_localidade_2.setText('')
            self.lineEdit_descricao_3.setText('')
            self.lineEdit_quantidade_3.setText('')
            self.lineEdit_valor_3.setText('')
            self.lineEdit_data_3.setText('')
            self.lineEdit_uberflash_2.setText('')
            self.lineEdit_impressao_2.setText('')
            self.lineEdit_outros_2.setText('')
            self.lineEdit_status_2.setText('')

            self.label_erro.setText('Dados Atualizado com sucesso!')
            self.frame_erro.setStyleSheet("background-color: green;")
            self.frame_erro.show()
            # Configurar um timer para ocultar o rótulo após 1 segundo
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.hide_message)
            self.timer.start(1500)  # 1000 ms = 1 segundo
        except:
            self.label_erro.setText('Falha ao atualizar')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()

    def deletar_linha_bd(self):
        procurar_nome = self.lineEdit_procurar.text()
        try:
            pessoa = str(run(bd.buscar_pessoa(procurar_nome))).replace("[","").replace("]","").replace(",",":")
            self.pessoa_registro = pessoa.split(':')
        
            venda = str(run(bd.buscar_id_venda(self.pessoa_registro[1]))).replace("[","").replace("]","")
            self.venda_registro = venda.split('.')

            despesas_venda = str(run(bd.buscar_id_despesas(self.venda_registro[1]))).replace("[","").replace("]","")
            self.despesas_venda_registro = despesas_venda.split(':')
            

            run(bd.deletar_pessoa(procurar_nome))
            run(bd.deletar_venda(self.venda_registro[1]))
            run(bd.deletar_despesasvenda(self.despesas_venda_registro[7]))

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

            self.label_erro.setText('Dados Atualizado com sucesso!')
            self.frame_erro.setStyleSheet("background-color: green;")
            self.frame_erro.show()
            # Configurar um timer para ocultar o rótulo após 1 segundo
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.hide_message)
            self.timer.start(1500)  # 1000 ms = 1 segundo

        except:
            self.label_erro.setText('Falha ao deletar\nCliente não encontrado!')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()

    def procurar_estoque(self):
        nome_estoque = self.lineEdit_form_procurar_nome.text()
        try:
            self.estoque_ = str(run(bd.buscar_fornecedor(nome_estoque))).replace("[","").replace("]","")
            self.estoque_list = self.estoque_.split('.')

            self.lineEdit_form_nome.setText(self.estoque_list[3])
            self.lineEdit_form_produto.setText(self.estoque_list[5])
            self.lineEdit_form_ecomerce.setText(self.estoque_list[13])
            self.lineEdit_form_quantidade.setText(self.estoque_list[7])
            self.lineEdit_form_valor.setText(self.estoque_list[9])
            self.lineEdit_form_data.setText(self.estoque_list[11])
        except:
            self.label_erro.setText('Cliente não encontrado no banco de dados!')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()

    def atualiza_estoque(self):
        try:
            nome_estoque = self.lineEdit_form_nome.text()
            produto_estoque = self.lineEdit_form_produto.text()
            e_comerce_estoque  = self.lineEdit_form_ecomerce.text()
            quantidade_estoque = self.lineEdit_form_quantidade.text()
            valor_estoque = self.lineEdit_form_valor.text()
            data_estoque = self.lineEdit_form_data.text()

            run(bd.atualizar_estoque_fornecedor(self.estoque_list[3],nome_estoque))
            run(bd.atualizar_estoque_produto(self.estoque_list[5],produto_estoque))
            run(bd.atualizar_estoque_ecomerce(self.estoque_list[13],e_comerce_estoque))
            run(bd.atualizar_estoque_qtde(self.estoque_list[1],quantidade_estoque))
            run(bd.atualizar_estoque_valor(self.estoque_list[9],valor_estoque))
            run(bd.atualizar_estoque_data_pedido(self.estoque_list[11],data_estoque))
        
        except:
            self.label_erro.setText('Campo em branco')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()

    def deletar_linha_estoque(self):
       
        nome_estoque = self.lineEdit_form_procurar_nome.text()
        nome_ = nome_estoque.replace("",'0')
        if nome_ == '0':
            self.label_erro.setText('Campo em branco')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()
        else:
            run(bd.deletar_linha_estoque(nome_estoque))

            self.lineEdit_form_nome.setText('')
            self.lineEdit_form_produto.setText('')
            self.lineEdit_form_ecomerce.setText('')
            self.lineEdit_form_quantidade.setText('')
            self.lineEdit_form_valor.setText('')
            self.lineEdit_form_data.setText('')
        
            self.label_erro.setText('Dados Deletado com sucesso!')
            self.frame_erro.setStyleSheet("background-color: green;")
            self.frame_erro.show()
            # Configurar um timer para ocultar o rótulo após 1 segundo
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.hide_message)
            self.timer.start(1500)  # 1000 ms = 1 segundo
    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
