"""import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

x = [1,2,3,4,5]
y = [3,2,4,3,2]

plt.bar(x,y,label='dados',color="r")
plt.ylabel('eixo y')
plt.xlabel('eixo x')
plt.title('Grafico loco')
plt.legend()
plt.show()"""

import BD_myframecg as bd
import pandas as pd

#lista
index = [
    'Produto',
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

#laço de repetição usando numero e elemento da lista
for num, i in enumerate(bd.venda()):
    #pegando primeiro valor da lista
    indice = index[num]
    df[indice] = df[indice].fillna('')
    #pegando o numero da coluna
    numero_coluna = df.columns.get_loc(indice)
    #transformando primeira linha da lista em str
    linha = str(i)
    #separando em outra lista a str obtida
    linha_str = linha.split(",")
    #fazendo uma comparação se o indice encontrado ex "Produto" é igual ao valor que esta na lista ex "valor"
    if indice == linha_str[num]:
        posicao = df.iloc[num + 1,numero_coluna]

        df.iloc[2,1] = linha_str[3]

    print(linha_str)
    


    df.to_excel('lol.xlsx')

   
  
