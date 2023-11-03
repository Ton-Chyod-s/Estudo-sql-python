import plotly.express as px
import BD_myframecg as bd
import pandas as pd
from datetime import datetime
from calendar import monthrange
import datetime

class tratamento_db:
    def __init__(self):
        pass
    
    def estoque_analise(self):
        #lista
        index = [
            'Fornecedor',
            'Produto',
            'Quantidade',
            'Valor',
            'Data pedido',
            'E-commerce'
        ]

        self.df = pd.DataFrame(index)
        #invertendo linha para coluna
        self.df = self.df.T
        #transformando primeira linha em indice
        self.df.columns = self.df.loc[0]
        #deletando primeira linha
        self.df = self.df.drop(range(1))
        #resete index linha
        self.df = self.df.reset_index(drop=True)

        for num, linha in enumerate(bd.estoque_()):
            linha_list = str(linha).split(".")
            for linha_index in index:
                for ince_linha_str in linha_list:
                    try:
                        linha_list_nv = ince_linha_str.split(':')
                        indice_linha = linha_list_nv[0]
                        valor_linha = linha_list_nv[1]
                    except Exception as e:
                        print(e)
                        
                    #fazendo uma comparação se o indice encontrado ex "Produto" é igual ao valor que esta na lista ex "valor"
                    if linha_index == indice_linha:
                        descricao_list = valor_linha.split('-')
                        #adicionando valor no data frame
                        self.df.at[num,linha_index] = valor_linha
                        break

        return self.df
    
    def vendas(self):
        valor_janeiro = {}
        valor_fevereiro = {}
        valor_marco = {}
        valor_abril = {}
        valor_maio = {}
        valor_junho = {}
        valor_julho = {}
        valor_agosto = {}
        valor_setembro = {}
        valor_outubro = {}
        valor_novembro = {}
        valor_dezembro = {}

        #lista
        index = [
            'Produto',
            'Quantidade',
            'Valor',
            'Data pedido',
            'Data prazo',
            'status',
            'Situação',
            'id',
        ]

        self.df = pd.DataFrame(index)
        #invertendo linha para coluna
        self.df = self.df.T
        #transformando primeira linha em indice
        self.df.columns = self.df.loc[0]
        #deletando primeira linha
        self.df = self.df.drop(range(1))
        #resete index linha
        self.df = self.df.reset_index(drop=True)

        #laço de repetição usando numero e elemento da lista
        for cliente, i in enumerate(bd.venda()):
                #transformando primeira linha da lista em str
                linha = str(i)
                #separando em outra lista a str obtida
                linha_str = linha.split(".")
                for linha_index in index:
                    #pegando primeiro valor da lista
                    try:
                        indice = linha_index
                    except:
                        break
                    for num, ince_linha_str in enumerate(linha_str):
                        try:    
                            nome_linha = ince_linha_str
                        except:
                            break
                        #fazendo uma comparação se o indice encontrado ex "Produto" é igual ao valor que esta na lista ex "valor"
                        if linha_index == nome_linha:
                            nome = indice
                            descricao = linha_str[num+1]
                            #print(f'{nome}: {descricao}\n')
                            self.df.at[cliente,indice] = descricao
                        #preencher dicionario para futuros calculo
                        try:
                            data = linha_str[9]
                            data_split = data.split("-")

                            def condicao(mes_num,mes_nome):
                                if data_split[0] == mes_num:
                                    valor_ = linha_str[7]
                                    mes_nome[cliente] = valor_
                            condicao("01",valor_janeiro)
                            condicao("02",valor_fevereiro)
                            condicao("03",valor_marco)
                            condicao("04",valor_abril)
                            condicao("05",valor_maio)
                            condicao("06",valor_junho)
                            condicao("07",valor_julho)
                            condicao("08",valor_agosto)
                            condicao("09",valor_setembro)
                            condicao("10",valor_outubro)
                            condicao("11",valor_novembro)
                            condicao("12",valor_dezembro)
                        except:
                            pass
        #dicionario com a soma total dos meses
        self.data_soma = {}
        #função para somar os valores no dicionarios
        def soma(dicionario,mes):
            soma = 0
            for i in dicionario:
                valores = str(dicionario[i]).replace(",",".")
                num = float(valores)
                soma += num
            self.data_soma[mes] = soma

        #dicionario e mês    
        soma(valor_janeiro,"janeiro")
        soma(valor_fevereiro,"fevereiro")
        soma(valor_marco,"marco")
        soma(valor_abril,"abril")
        soma(valor_maio,"maio")
        soma(valor_junho,"junho")
        soma(valor_julho,"julho")
        soma(valor_agosto,"agosto")
        soma(valor_setembro,"setembro")
        soma(valor_outubro,"outubro")
        soma(valor_novembro,"novembro")
        soma(valor_dezembro,"dezembro")

        return self.df
    
    def cliente_s(self):
        index = [
            'id',
            'nome',
            'e-mail',
            'whats-app',
            'localidade',
            'contato'
        ]
        self.df = pd.DataFrame(index)
        #invertendo linha para coluna
        self.df = self.df.T
        #transformando primeira linha em indice
        self.df.columns = self.df.loc[0]
        #deletando primeira linha
        self.df = self.df.drop(range(1))
        #resete index linha
        self.df = self.df.reset_index(drop=True)
        #laço de repetição usando numero e elemento da lista
        for num, i in enumerate(bd.clientes()):
                #transformando primeira linha da lista em str
                linha = str(i)
                #separando em outra lista a str obtida
                linha_str = linha.split(",")
                for linha_index in index:
                    #pegando primeiro valor da lista
                    try:
                        indice = linha_index
                    except:
                        break
                    for ince_linha_str in linha_str:
                        try:    
                            nome_linha = ince_linha_str
                            linha_list = nome_linha.split(':')
                            indice_linha = linha_list[0]
                            valor_linha = linha_list[1]
                        except:
                            break
                        #fazendo uma comparação se o indice encontrado ex "Produto" é igual ao valor que esta na lista ex "valor"
                        if linha_index == indice_linha:
                            descricao_list = valor_linha.split('-')
                            #adicionando valor no data frame
                            self.df.at[num,indice] = valor_linha
                            if '-' in valor_linha:
                                #teste para ver se existe complemento no nome ex ELO7
                                contato = descricao_list[1]
                                self.df.at[num,'contato'] = contato
                            celula = celula = self.df.at[num,'contato']
                            if pd.isna(celula):
                                self.df.at[num,'contato'] = 'Whats-app'
                            break
        return self.df

    def vendas_adicionais(self):
        data_atual = datetime.today()
        tabela = self.vendas()
        for index_linha, i in enumerate(tabela['Data pedido']):
            
            data_lis = i.split("-")
            mes = int(data_lis[0])
            dia = int(data_lis[1])
            ano = int(data_lis[2])
            data = datetime(ano,mes,dia)
            prazo_dia = dia + 4
             # Obter o último dia do mês
            ultimo_dia = monthrange(ano, mes)[1]

            # Verificar se o prazo ultrapassa o último dia do mês
            if prazo_dia > ultimo_dia:
                prazo_dia = ultimo_dia  # Definir o prazo para o último dia do mês

            data_prazo = datetime(ano, mes, prazo_dia)

            
            if prazo_dia > ultimo_dia:
                prazo_dia = prazo_dia - ultimo_dia
                mes = mes + 1

            elif mes == 2:
                if prazo_dia > ultimo_dia:
                    prazo_dia = prazo_dia - ultimo_dia 
                    mes = mes + 1

            #pegando informação no data frame
            status = self.df.at[index_linha,'status']
    
            data_prazo = datetime(ano,mes,prazo_dia)
            #formatar data
            data_em_texto = '{}/{}/{}'.format(data_prazo.day,data_prazo.month,data_prazo.year)
            #formatar data
            data_texto = '{}/{}/{}'.format(data.day,data.month,data.year)

            #adicionar no dataframe o prazo
            self.df.at[index_linha,'Data prazo'] = data_em_texto
            #adicionar no dataframe Data
            self.df.at[index_linha,'Data pedido'] = data_texto
            
            if data_prazo.date() < data_atual.date() and status != 'Concluido':
                calculo = (data_atual.date() - data_prazo.date()).days
                self.df.at[index_linha,'Situação'] = f'Fora do prazo, {calculo} dias'
            else:
                if status == 'Concluido':
                    self.df.at[index_linha,'Situação'] = 'Produto enviado'
                else:
                    self.df.at[index_linha,'Situação'] = 'Dentro do prazo'
                
        return self.df

    def planilha_completa(self):
        #data frame
        frame_vendas = self.vendas_adicionais()
        frame_clientes = self.cliente_s()
        #juntando os dois data frame pelo id
        tabela = pd.merge(frame_clientes, frame_vendas, on="id")
        
        self.df = pd.DataFrame(tabela)
        return self.df

    def salvar(self,nome):
        #salvando em excel 
        self.df.to_excel(nome, index=False)   

    def grafico_barra(self):
        #configuração do grafico
        meses = []
        valor_tot = []
        for valor in self.data_soma:
            meses.append(valor)
            valor_total = self.data_soma[valor]
            valor_tot.append(valor_total)

        self.x = meses
        self.y = valor_tot

        fig = px.bar(self.df,x=self.x, y=self.y,height = 450,width=650 , labels={'x': '','y': ''},template='none',color_discrete_sequence=px.colors.qualitative.Prism)
        fig.update_traces(textposition='outside',texttemplate='%{y:.4s}')
        fig.update_yaxes(visible=False)
        fig.update_layout(title={'text' : 'Venda x Mês',})
        fig.show()

    def dre(self):
        data_atual = datetime.date.today()
        ano_atual = data_atual.year
        
        index = [
            'Descrição','Janeiro','Av','Fevereiro','Av','Março','Av','Abril','Av','Maio','Av',
            'Junho','Av','Julho','Av','Agosto','Av','Setembro','Av','Outubro','Av','Novembro',
            'Av','Dezembro','Av'
        ]

        self.df = pd.DataFrame(index)
        #invertendo linha para coluna
        self.df = self.df.T
        #transformando primeira linha em indice
        self.df.columns = self.df.loc[0]
        #deletando primeira linha
        self.df = self.df.drop(range(1))
        #resete index linha
        self.df = self.df.reset_index(drop=True)

        for num, linha in enumerate(bd.dre_()):
            for linha_index in index:
                try:
                    linha_list = str(linha).split(":")
                    indice_linha = linha_list[0]
                    valor_linha = linha_list[1]
                except Exception as e:
                    print(e)
                    
                #fazendo uma comparação se o indice encontrado ex "Produto" é igual ao valor que esta na lista ex "valor"
                if linha_index == indice_linha:
                    descricao_list = valor_linha.split('-')
                    #adicionando valor no data frame
                    self.df.at[num,linha_index] = valor_linha
                    break

        valor_janeiro = 0
        valor_fevereiro = 0 
        valor_marco = 0
        valor_abril = 0
        valor_maio = 0
        valor_junho = 0
        valor_julho = 0
        valor_agosto = 0
        valor_setembro = 0
        valor_outubro = 0
        valor_novembro = 0
        valor_dezembro = 0

        for cliente, i in enumerate(bd.venda()):
            try:
                #linha que transforma o i em string logo em seguida em uma lista pegando o valor 7 dessa lista no final transforma em inteiro
                valor_lis = str(i).split(".")
                data_ = valor_lis[9].split("-")
                mes = int(data_[0])
                ano = int(data_[2])
                valor_lista = float(valor_lis[7].replace(",","."))
                if mes == 1 and ano == ano_atual:
                    valor_janeiro += valor_lista

                if mes == 2 and ano == ano_atual:
                    valor_fevereiro += valor_lista

                if mes == 3 and ano == ano_atual:
                    valor_marco += valor_lista

                if mes == 4 and ano == ano_atual:
                    valor_abril += valor_lista

                if mes == 5 and ano == ano_atual:
                    valor_maio += valor_lista

                if mes == 6 and ano == ano_atual:
                    valor_junho += valor_lista

                if mes == 7 and ano == ano_atual:
                    valor_julho += valor_lista

                if mes == 8 and ano == ano_atual:
                    valor_agosto += valor_lista

                if mes == 9 and ano == ano_atual:
                    valor_setembro += valor_lista

                if mes == 10 and ano == ano_atual:
                    valor_outubro += valor_lista

                if mes == 11 and ano == ano_atual:
                    valor_novembro += valor_lista

                if mes == 12 and ano == ano_atual:
                    valor_dezembro += valor_lista

            except Exception as e:
                print(e)

        """for cliente, i in enumerate(bd.estoque_()):
            try:
                #linha que transforma o i em string logo em seguida em uma lista pegando o valor 7 dessa lista no final transforma em inteiro
                valor_lis = str(i).split(".")
               
                data = str(valor_lis[11])
                mes = int(data.split("/")[1])
                ano = int(data.split("/")[2])
                linha_lista = float(valor_lis[9].replace(",","."))
            
                if mes == 1 and ano == ano_atual:
                    valor_janeiro -= linha_lista

                if mes == 2 and ano == ano_atual:
                    valor_fevereiro -= linha_lista

                if mes == 3 and ano == ano_atual:
                    valor_marco -= linha_lista

                if mes == 4 and ano == ano_atual:
                    valor_abril -= linha_lista

                if mes == 5 and ano == ano_atual:
                    valor_maio -= linha_lista

                if mes == 6 and ano == ano_atual:
                    valor_junho -= linha_lista

                if mes == 7 and ano == ano_atual:
                    valor_julho -= linha_lista

                if mes == 8 and ano == ano_atual:
                    valor_agosto -= linha_lista

                if mes == 9 and ano == ano_atual:
                    valor_setembro -= linha_lista

                if mes == 10 and ano == ano_atual:
                    valor_outubro -= linha_lista

                if mes == 11 and ano == ano_atual:
                    valor_novembro -= linha_lista

                if mes == 12 and ano == ano_atual:
                    valor_dezembro -= linha_lista
            

            except Exception as e:
                print(e)"""

        return self.df

if __name__ == '__main__':
    tr = tratamento_db()
    #tr.vendas()
    #tr.grafico_barra()
    #tr.cliente_s()
    #tr.planilha_completa()
    #tr.data_prazo()
    #tr.estoque_analise()
    tr.dre()
    tr.salvar('dre.xlsx',)
    

    

    