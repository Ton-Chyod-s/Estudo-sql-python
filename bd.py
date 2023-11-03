import pandas as pd
import datetime

df_vendas = pd.read_excel('VENDA 2023.xlsx',sheet_name='VENDAS')
df_despesas = pd.read_excel('VENDA 2023.xlsx',sheet_name='DESPESAS')

venda_2023 = []
estoque_2023 = []

# Itera sobre as linhas do DataFrame e imprime os valores de cada coluna
for index, row in df_vendas.iterrows():
    nome = row['NOME']
    e_mail = '@'
    whats_app = '67 99999999'
    localidade = 'campo grande'
    produto = row['PRODUTO']
    quantidade = row['QTDE']
    valor = str(row['VALOR']).replace(",",'.')
    data_pedido = str(row['DATA']).split(" ")[0]
    data_pedido_certo = data_pedido.split("-")
    data_pedido_formt = '{}/{}/{}'.format(data_pedido_certo[2],data_pedido_certo[1],data_pedido_certo[0])
    uberflash = row['UBER FLASH']
    situacao = row['SITUAÇÃO']
    status = row['STATUS']
    impressao = row['IMPRESSÃO']
    outros = '0'
    linha_completa = f'{nome},{e_mail},{whats_app},{localidade},{produto},{quantidade},{valor},{data_pedido_formt},{uberflash},{impressao},{status}'
    venda_2023.append(linha_completa)

# Itera sobre as linhas do DataFrame e imprime os valores de cada coluna
for index, row in df_despesas.iterrows():
    nome_loja = row['NOME LOJA']
    produto = row['PRODUTO']
    quantidade = row['QTDE']
    valor = row['VALOR']
    data = str(row['DATA']).split(" ")[0]
    data_pedido_certo = data.split("-")
    data_pedido_formt = '{}/{}/{}'.format(data_pedido_certo[2],data_pedido_certo[1],data_pedido_certo[0])
    entrega = row['ENTREGA']
    linha_completa = f'{nome_loja}.{produto}.{quantidade}.{valor}.{data_pedido_formt}.{entrega}'
    estoque_2023.append(linha_completa)  
    


dre_2023 = [
    'RECEITA BRUTA',
    '(-) DEVOLUÇÕES/CANCELAMENTO',
    'RECEITA LÍQUIDA',
    '(-) CUSTO DE PROCDUTOS VENDIDOS/CPV',
    '(-) ENTRADA DE MERCADORIA',
    'LUCRO BRUTO',
    '(-) DESPESAS/RECEITAS OPERACIONAIS GERAIS E ADM',
    'PRO LABORE',
    'TI',
    '(-) OUTRAS DESPESAS/RECEITAS',
    'UBER FLASH',
    'SITE',
    'DNS',
    'MARKETING',
    'NUVEM DE ARQUIVOS',
    '(+) OUTRAS RECEITAS',
    'INVESTIMENTO',
    'RESULTADO DO MES ANTERIOR',
    'RESULTADO FINANCEIRO',
    '(-) IR/CS',
    'CPNJ',
    'LUCRO LIQUIDO'
]

