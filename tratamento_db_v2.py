import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import BD_myframecg as bd
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

class tratamento_db:
    def __init__(self):
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
            'Cliente id',
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
                            data = linha_str[7]
                            data_split = data.split("-")

                            def condicao(mes_num,mes_nome):
                                if data_split[0] == mes_num:
                                    valor_ = linha_str[5]
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
    
    def data_frame(self):
        return self.df

    def salvar(self):
        #salvando em excel 
        self.df.to_excel('vendas.xlsx', index=False)   

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

        fig = px.bar(self.df,x=self.x, y=self.y,height = 450,width=700 , labels={'x': '','y': ''},template='none',color_discrete_sequence=px.colors.qualitative.Prism)
        fig.update_traces(textposition='outside',texttemplate='%{y:.4s}')
        fig.update_yaxes(showticklabels=False)
        fig.update_layout(title={
        'text' : 'Venda x Mês',
    })
        fig.show()

if __name__ == '__main__':
    tr = tratamento_db()
    tr.grafico_barra()

    

    