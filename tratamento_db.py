import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import BD_myframecg as bd
import pandas as pd



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

df = pd.DataFrame(index)
#invertendo linha para coluna
df = df.T
#transformando primeira linha em indice
df.columns = df.loc[0]
#deletando primeira linha
df = df.drop(range(1))
#resete index linha
df = df.reset_index(drop=True)

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
                    df.at[cliente,indice] = descricao
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
data_soma = {}
#função para somar os valores no dicionarios
def soma(dicionario,mes):
    soma = 0
    for i in dicionario:
        valores = str(dicionario[i]).replace(",",".")
        num = float(valores)
        soma += num
    data_soma[mes] = soma

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

def salvar():
    #salvando em excel 
    df.to_excel('vendas.xlsx', index=False)   

def grafico_barra():
    #configuração do grafico
    meses = []
    valor_tot = []
    for valor in data_soma:
        meses.append(valor)
        valor_total = data_soma[valor]
        valor_tot.append(valor_total)

    x = meses
    y = valor_tot

    plt.bar(x,y,label='dados',color="r")
    plt.title('Venda x mês')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    grafico_barra()
    salvar()

