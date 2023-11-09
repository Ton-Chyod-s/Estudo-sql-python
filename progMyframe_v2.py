from main import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import BD_myframecg as bd
from asyncio import run
import os
from PyQt6.QtCore import QTimer
import tratamento_db_v2 as tr
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
                nome = isEmpty(self.lineEdit_nome_2.text())
                telefone = isEmpty(self.lineEdit_telefone_2.text())
                email = isEmpty(self.lineEdit_email_2.text())
                localidade = isEmpty(self.lineEdit_localidade_2.text())
                descricao = isEmpty(self.lineEdit_descricao_3.text())
                quantidade = isEmpty(self.lineEdit_quantidade_3.text())
                valor = isEmpty(self.lineEdit_valor_3.text())
                data = isEmpty(self.lineEdit_data_3.text())
                uberflash = isEmpty(self.lineEdit_uberflash_2.text())
                impressao = isEmpty(self.lineEdit_impressao_2.text())
                outros = isEmpty(self.lineEdit_outros_2.text())
                status = isEmpty(self.lineEdit_status_2.text())

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
            
        nome = isEmpty(self.estoque_popup.lineEdit_form_nome.text())
        if nome == None:
            self.label_erro.setText('Campo em branco')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()
        else:    
            produto = isEmpty(self.estoque_popup.lineEdit_form_produto.text())
            ecomerce = isEmpty(self.estoque_popup.lineEdit_form_ecomerce.text())
            quantidade = isEmpty(self.estoque_popup.lineEdit_form_quantidade.text())
            valor = isEmpty(self.estoque_popup.lineEdit_form_valor.text())
            data = isEmpty(self.estoque_popup.lineEdit_form_data.text())

            run(bd.estoque(nome,produto,quantidade,valor,data,ecomerce))

            self.estoque_popup.lineEdit_form_nome.setText('')
            self.estoque_popup.lineEdit_form_produto.setText('')
            self.estoque_popup.lineEdit_form_ecomerce.setText('')
            self.estoque_popup.lineEdit_form_quantidade.setText('')
            self.estoque_popup.lineEdit_form_valor.setText('')
            self.estoque_popup.lineEdit_form_data.setText('')

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
    
    def popup(self):
        from popup import Ui_MainWindow_estoque

        self.janela = QtWidgets.QMainWindow()
        self.estoque_popup = Ui_MainWindow_estoque()
        self.estoque_popup.setupUi(self.janela)
        self.janela.show()
        qt.exec()

    def estoque(self):
        from estoque import Ui_MainWindow_estoque

        
        self.janela = QtWidgets.QMainWindow()
        self.estoque_popup = Ui_MainWindow_estoque()
        self.estoque_popup.setupUi(self.janela)
        self.estoque_popup.pushButton_form_inserir.clicked.connect(self.inserir_estoque)
        self.estoque_popup.pushButton_form_atualizar.clicked.connect(self.atualizar_estoque)
        self.estoque_popup.pushButton_form_deletar.clicked.connect(self.deletar_estoque)
        self.estoque_popup.pushButton_form_procurar.clicked.connect(self.procurar_estoque)
        self.estoque_popup.pushButton_form_salvar.clicked.connect(self.salvar_estoque)

        self.janela.show()
        qt.exec()

    def atualizar_estoque(self):
        
        def isEmpty(txt):
            if txt == '':
                txt = 'vazio'
            else:
                return txt

        #pegando as informações digitada pelo usuario
        nome = isEmpty(self.estoque_popup.lineEdit_form_nome.text())
        produto = isEmpty(self.estoque_popup.lineEdit_form_produto.text())
        ecommerce = isEmpty(self.estoque_popup.lineEdit_form_ecomerce.text())
        qtde = isEmpty(self.estoque_popup.lineEdit_form_quantidade.text())
        valor = isEmpty(self.estoque_popup.lineEdit_form_valor.text())
        data = isEmpty(self.estoque_popup.lineEdit_form_data.text())
 
        
        self.estoque_ = str(run(bd.buscar_fornecedor(nome))).replace("[","").replace("]","")
        lol = self.estoque_.split(", ")

        for i in lol:
            self.estoque_list = i.split('.')
        
        nome_db = self.estoque_list[3]
        produto_db = self.estoque_list[5]
        ecommerce_db = self.estoque_list[13]
        qtde_db = self.estoque_list[7]
        valor_db = self.estoque_list[9]
        data_db = self.estoque_list[11]

        run(bd.atualizar_estoque_fornecedor(nome_db,nome))
        run(bd.atualizar_estoque_produto(produto_db,produto))
        run(bd.atualizar_estoque_ecomerce(ecommerce_db,ecommerce))
        #run(bd.atualizar_estoque_qtde(qtde_db,qtde))
        #run(bd.atualizar_estoque_valor(valor_db,valor))
        #run(bd.atualizar_estoque_data_pedido(data_db,data))

        print('chego até aqui')

    def deletar_estoque(self):
        try:
            def isEmpty(txt):
                if txt == '':
                    txt = 'vazio'
                else:
                    return txt
                
            nome = isEmpty(self.estoque_popup.lineEdit_form_nome.text())

            run(bd.deletar_linha_estoque(nome))

            self.estoque_popup.lineEdit_form_nome.setText('')
            self.estoque_popup.lineEdit_form_produto.setText('')
            self.estoque_popup.lineEdit_form_ecomerce.setText('')
            self.estoque_popup.lineEdit_form_quantidade.setText('')
            self.estoque_popup.lineEdit_form_valor.setText('')
            self.estoque_popup.lineEdit_form_data.setText('')

            self.label_erro.setText('Dados deletado!')
            self.frame_erro.setStyleSheet("background-color: green;")
            self.frame_erro.show()
            # Configurar um timer para ocultar o rótulo após 1 segundo
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.hide_message)
            self.timer.start(1500)  # 1000 ms = 1 segundo
        except:
            self.label_erro.setText('Dados não encontrar!')
            self.frame_erro.setStyleSheet("background-color: red;")
            self.frame_erro.show()
            # Configurar um timer para ocultar o rótulo após 1 segundo
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.hide_message)
            self.timer.start(1500)  # 1000 ms = 1 segundo
        
    def salvar_estoque(self):
        tratamento = tr.tratamento_db()
        tratamento.estoque_analise()
        tratamento.salvar('Estoque.xlsx',)

    def custos_fixos(self):
        from custos_fixos import Ui_MainWindow_estoque
        self.janela = QtWidgets.QMainWindow()
        self.estoque_ = Ui_MainWindow_estoque()
        self.estoque_.setupUi(self.janela)
        self.estoque_.pushButton_form_inserir.clicked.connect(self.inserir_custos)
        self.estoque_.pushButton_form_atualizar.clicked.connect(self.atualizar_custos)
        self.estoque_.pushButton_form_deletar.clicked.connect(self.deletar_custos)
        self.estoque_.pushButton_form_procurar.clicked.connect(self.procurar_custos)
        self.estoque_.pushButton_form_salvar.clicked.connect(self.salvar_custos)

        self.janela.show()
        qt.exec()

    def inserir_custos(self):
        def isEmpty(txt):
            if txt == '':
                txt = 'vazio'
            else:
                return txt
        
        pro_labore = isEmpty(self.estoque_.lineEdit_form_nome.text())
        ti = isEmpty(self.estoque_.lineEdit_form_produto.text())
        site = isEmpty(self.estoque_.lineEdit_form_ecomerce.text())
        dns = isEmpty(self.estoque_.lineEdit_form_quantidade.text())
        marketing = isEmpty(self.estoque_.lineEdit_form_valor.text())
        nuvem_arquivos = isEmpty(self.estoque_.lineEdit_form_data.text())

        if pro_labore == None:
            pro_labore = 0
        if ti == None:
            ti = 0
        if site == None:
            site = 0
        if dns == None:
            dns = 0
        if marketing == None:
            marketing = 0
        if nuvem_arquivos == None:
            nuvem_arquivos = 0
        
        try:
            run(bd.custos_fixos(pro_labore,ti,site,dns,marketing,nuvem_arquivos))
        except:
            pass

        self.estoque_.lineEdit_form_nome.setText('')
        self.estoque_.lineEdit_form_produto.setText('')
        self.estoque_.lineEdit_form_ecomerce.setText('')
        self.estoque_.lineEdit_form_quantidade.setText('')
        self.estoque_.lineEdit_form_valor.setText('')
        self.estoque_.lineEdit_form_data.setText('')
        
        
        principal.show()
        qt.exec()

    def atualizar_custos(self):
        
        def isEmpty(txt):
                if txt == '':
                    txt = 'vazio'
                else:
                    return txt
            
        pro_labore = isEmpty(self.estoque_.lineEdit_form_nome.text())
        ti = isEmpty(self.estoque_.lineEdit_form_produto.text())
        site = isEmpty(self.estoque_.lineEdit_form_ecomerce.text())
        dns = isEmpty(self.estoque_.lineEdit_form_quantidade.text())
        marketing = isEmpty(self.estoque_.lineEdit_form_valor.text())
        nuvem_arquivos = isEmpty(self.estoque_.lineEdit_form_data.text())

        
        linha = self.tratamento.custos_fixos()
        linha_list = linha.iloc[0]
        pro_abore_db = int(linha_list.loc['Pro Labore'])
        ti_db = int(linha_list.loc['TI'])
        site_db = int(linha_list.loc['Site'])
        dns_db = int(linha_list.loc['DNS'])
        marketing_db = int(linha_list.loc['Marketing'])
        nuvem_arquivos_db = int(linha_list.loc['Nuvem de arquivos'])


        run(bd.atualizar_custo_pro_labore(pro_abore_db,pro_labore))
        run(bd.atualizar_custo_ti(ti_db,ti))
        run(bd.atualizar_custo_site(site_db,site))
        run(bd.atualizar_custo_dns(dns_db,dns))
        run(bd.atualizar_custo_marketing(marketing_db,marketing))
        run(bd.atualizar_custo_nuvem_arquivos(nuvem_arquivos_db,nuvem_arquivos))

    def deletar_custos(self):
        try:
            pro_labore = self.estoque_.lineEdit_form_nome.text()
        
            run(bd.deletar_linha_custo(pro_labore))
            
            self.estoque_.lineEdit_form_nome.setText('')
            self.estoque_.lineEdit_form_produto.setText('')
            self.estoque_.lineEdit_form_ecomerce.setText('')
            self.estoque_.lineEdit_form_quantidade.setText('')
            self.estoque_.lineEdit_form_valor.setText('')
            self.estoque_.lineEdit_form_data.setText('')
            
        except:
            pass
        
    def procurar_custos(self):
        try:
            id = self.estoque_.lineEdit_form_procurar_nome.text()
        
            id_name = str(run(bd.buscar_custos(id))).replace("[","").replace("]","")
            id_list = id_name.split(",")

            self.estoque_.lineEdit_form_nome.setText(id_list[1])
            self.estoque_.lineEdit_form_produto.setText(id_list[3])
            self.estoque_.lineEdit_form_ecomerce.setText(id_list[5])
            self.estoque_.lineEdit_form_quantidade.setText(id_list[7])
            self.estoque_.lineEdit_form_valor.setText(id_list[9])
            self.estoque_.lineEdit_form_data.setText(id_list[11])
        except:
            pass

    def salvar_custos(self):
        tratamento = tr.tratamento_db()
        tratamento.custos_fixos()
        tratamento.salvar('Custos Fixos.xlsx',)
        
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
        nome_estoque = self.estoque_popup.lineEdit_form_procurar_nome.text()
        
        try:
            self.estoque_ = str(run(bd.buscar_fornecedor(nome_estoque))).replace("[","").replace("]","")
            lol = self.estoque_.split(", ")

            for i in lol:
                self.estoque_list = i.split('.')
            
            self.estoque_popup.lineEdit_form_nome.setText(self.estoque_list[3])
            self.estoque_popup.lineEdit_form_produto.setText(self.estoque_list[5])
            self.estoque_popup.lineEdit_form_ecomerce.setText(self.estoque_list[13])
            self.estoque_popup.lineEdit_form_quantidade.setText(self.estoque_list[7])
            self.estoque_popup.lineEdit_form_valor.setText(self.estoque_list[9])
            self.estoque_popup.lineEdit_form_data.setText(self.estoque_list[11])

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
