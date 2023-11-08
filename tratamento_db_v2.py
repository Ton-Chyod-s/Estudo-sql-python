import plotly.express as px
import BD_myframecg as bd
import pandas as pd
from datetime import date
from calendar import monthrange
import datetime
from time import sleep

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
                cont = 0
                for ince_linha_str in linha_list:
                    try:
                        linha_list_nv = ince_linha_str.split(':')
                        valor_linha = linha_list[cont + 1]
                        
                    except Exception as e:
                        print(e)
                    cont += 1

                    #fazendo uma comparação se o indice encontrado ex "Produto" é igual ao valor que esta na lista ex "valor"
                    if linha_index == linha_list_nv[0]:
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
                linha_str = linha.split(",")
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
        data_atual = date.today()
        tabela = self.vendas()
        for index_linha, i in enumerate(tabela['Data pedido']):
            data_lis = i.split("/")
            dia = int(data_lis[0])
            mes = int(data_lis[1])
            ano = int(data_lis[2])
            data = date(ano,mes,dia)
            prazo_dia = dia + 4
             # Obter o último dia do mês
            ultimo_dia = monthrange(ano, mes)[1]

            # Verificar se o prazo ultrapassa o último dia do mês
            if prazo_dia > ultimo_dia:
                prazo_dia = ultimo_dia  # Definir o prazo para o último dia do mês

            data_prazo = date(ano, mes, prazo_dia)

            if prazo_dia > ultimo_dia:
                prazo_dia = prazo_dia - ultimo_dia
                mes = mes + 1

            elif mes == 2:
                if prazo_dia > ultimo_dia:
                    prazo_dia = prazo_dia - ultimo_dia 
                    mes = mes + 1

            #pegando informação no data frame
            status = str(self.df.at[index_linha,'status']).lower()
    
            #formatar data
            data_em_texto = '{}/{}/{}'.format(data_prazo.day,data_prazo.month,data_prazo.year)
            #formatar data
            data_texto = '{}/{}/{}'.format(data.day,data.month,data.year)

            #adicionar no dataframe o prazo
            self.df.at[index_linha,'Data prazo'] = data_em_texto
            #adicionar no dataframe Data
            self.df.at[index_linha,'Data pedido'] = data_texto
            if status != 'concluído':
                calculo = (data_atual - data_prazo).days
                self.df.at[index_linha,'Situação'] = f'Fora do prazo, {calculo} dias'
            else:
                if status == 'concluído':
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
            'Descrição','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro',
            'Outubro','Novembro',
            'Dezembro'
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
        
        despesa_janeiro = 0
        despesa_fevereiro = 0 
        despesa_marco = 0
        despesa_abril = 0
        despesa_maio = 0
        despesa_junho = 0
        despesa_julho = 0
        despesa_agosto = 0
        despesa_setembro = 0
        despesa_outubro = 0
        despesa_novembro = 0
        despesa_dezembro = 0

        for num, i in enumerate(bd.venda()):
            #linha que transforma o i em string logo em seguida em uma lista pegando o valor 7 dessa lista no final transforma em inteiro
            valor_lis = str(i).split(",")
            data_ = valor_lis[9].split("/")
            mes = int(data_[1])
            ano = int(data_[2])
            valor_lista = float(valor_lis[7].replace(",","."))
            if ano == ano_atual:
                if mes == 1 :
                    valor_janeiro += valor_lista     
                elif mes == 2 :
                    valor_fevereiro += valor_lista
                elif mes == 3 :
                    valor_marco += valor_lista    
                elif mes == 4 :
                    valor_abril += valor_lista
                elif mes == 5 :
                    valor_maio += valor_lista
                elif mes == 6 :
                    valor_junho += valor_lista
                elif mes == 7 :
                    valor_julho += valor_lista
                elif mes == 8 :
                    valor_agosto += valor_lista
                elif mes == 9 :
                    valor_setembro += valor_lista
                elif mes == 10 :
                    valor_outubro += valor_lista
                elif mes == 11 :
                    valor_novembro += valor_lista
                elif mes == 12 :
                    valor_dezembro += valor_lista

        for cliente, i in enumerate(bd.estoque_()):
            try:
                #linha que transforma o i em string logo em seguida em uma lista pegando o valor 7 dessa lista no final transforma em inteiro
                valor_lis = str(i).split(".")
                data = str(valor_lis[11])
                mes = int(data.split("/")[1])
                ano = int(data.split("/")[2])
                linha_lista = float(valor_lis[9].replace(",","."))
            
                if mes == 1 and ano == ano_atual:
                    despesa_janeiro -= linha_lista
                elif mes == 2 and ano == ano_atual:
                    despesa_fevereiro -= linha_lista
                elif mes == 3 and ano == ano_atual:
                    despesa_marco -= linha_lista
                elif mes == 4 and ano == ano_atual:
                    despesa_abril -= linha_lista
                elif mes == 5 and ano == ano_atual:
                    despesa_maio -= linha_lista
                elif mes == 6 and ano == ano_atual:
                    despesa_junho -= linha_lista
                elif mes == 7 and ano == ano_atual:
                    despesa_julho -= linha_lista
                elif mes == 8 and ano == ano_atual:
                    despesa_agosto -= linha_lista
                elif mes == 9 and ano == ano_atual:
                    despesa_setembro -= linha_lista
                elif mes == 10 and ano == ano_atual:
                    despesa_outubro -= linha_lista
                elif mes == 11 and ano == ano_atual:
                    despesa_novembro -= linha_lista
                elif mes == 12 and ano == ano_atual:
                    despesa_dezembro -= linha_lista
            except Exception as e:
                print(e)

        def preencher_dre(mes_nome,porcentagem_nome,biblioteca_mes,biblioteca_despesas):
            try:
                def jan_df(linha,valor,porcentagem):
                    self.df.at[linha,mes_nome] = valor
                #receita bruta
                jan_df(0,biblioteca_mes,1)
                #devolução
                devolucao = 0
                porcentagem_devolucao = devolucao / biblioteca_mes
                jan_df(1,devolucao,porcentagem_devolucao)
                #receita liquida
                receita_liquida = biblioteca_mes - devolucao
                porcentagem_receita = receita_liquida / biblioteca_mes
                jan_df(2,receita_liquida,porcentagem_receita)
                #CUSTO DE PROCDUTOS VENDIDOS/CPV
                porcentagem_custo_vendidos = biblioteca_despesas * -1 / biblioteca_mes
                jan_df(3,biblioteca_despesas * -1,porcentagem_custo_vendidos)
                #ENTRADA DE MERCADORIA
                porcentagem_custo_vendidos = biblioteca_despesas * -1 / biblioteca_mes
                jan_df(4,biblioteca_despesas * -1,porcentagem_custo_vendidos)
                #LUCRO BRUTO
                lucro_bruto = ((biblioteca_despesas * -1) - receita_liquida) * -1
                porcentagem_lucro_bruto = lucro_bruto / biblioteca_mes
                jan_df(5,lucro_bruto,porcentagem_lucro_bruto)
                #PRO LABORE
                pro_labore = biblioteca_mes * 0.12
                porcentagem_pro_labore = pro_labore / biblioteca_mes
                jan_df(7,pro_labore,porcentagem_pro_labore)
                #TI
                ti = 45
                porcentagem_ti = ti / biblioteca_mes
                jan_df(8,ti,porcentagem_ti)
                #DESPESAS/RECEITAS OPERACIONAIS GERAIS E ADM
                despesas_gerais = pro_labore + ti
                porcentagem_despesas_gerais = despesas_gerais / biblioteca_mes
                jan_df(6,despesas_gerais,porcentagem_despesas_gerais)
                #UBER FLASH
                uber_flash = 0 / 12
                porcentagem_uber_flash = uber_flash  / biblioteca_mes 
                jan_df(10,uber_flash,porcentagem_uber_flash)
                #SITE
                site = 468 / 12
                porcentagem_site = site  / biblioteca_mes
                jan_df(11,site ,porcentagem_site)
                #DNS
                dns = 50 / 12
                porcentagem_dns = dns  / biblioteca_mes
                jan_df(12,dns ,porcentagem_dns)
                #MARKETING
                marketing = 40 / 12
                porcentagem_marketing = marketing  / biblioteca_mes
                jan_df(13,marketing ,porcentagem_marketing)
                #NUVEM DE ARQUIVOS
                nuvem_arquivos = 0 / 12
                porcentagem_nuvem_arquivos = nuvem_arquivos  / biblioteca_mes
                jan_df(14,nuvem_arquivos ,porcentagem_nuvem_arquivos)
                #OUTRAS DESPESAS/RECEITAS
                outras_despesas_receitas = uber_flash + site + dns + marketing + nuvem_arquivos
                porcentagem_outras_despesas = outras_despesas_receitas / biblioteca_mes
                jan_df(9,outras_despesas_receitas,porcentagem_outras_despesas)
                #INVESTIMENTO
                investimento = 150
                porcentagem_investimento = investimento / biblioteca_mes
                jan_df(16,investimento,porcentagem_investimento)
                #RESULTADO DO MES ANTERIOR
                resultado_anterior = 1
                porcentagem_resultado_anterior = resultado_anterior / biblioteca_mes
                jan_df(17,resultado_anterior,porcentagem_resultado_anterior)
                #OUTRAS RECEITAS
                outras_receitas = investimento + resultado_anterior
                porcentagem_outras_receitas = outras_receitas / biblioteca_mes
                jan_df(15,outras_receitas,porcentagem_outras_receitas)
                #RESULTADO FINANCEIRO
                resultado_financeiro = lucro_bruto - despesas_gerais - outras_despesas_receitas + outras_receitas
                porcentagem_resultado_financeiro = resultado_financeiro / biblioteca_mes
                jan_df(18, resultado_financeiro , porcentagem_resultado_financeiro)
                #IR/CS
                ir_cs = 0
                porcentagem_ir_cs = ir_cs / biblioteca_mes
                jan_df(19,ir_cs,porcentagem_ir_cs)
                #CPNJ
                cnpj = 0
                porcentagem_cnpj = cnpj / biblioteca_mes
                jan_df(20,cnpj,porcentagem_cnpj)
                #LUCRO LIQUIDO
                lucro_liquido = resultado_financeiro - ir_cs - cnpj
                porcentagem_lucro_liquido = lucro_liquido / biblioteca_mes
                jan_df(21,lucro_liquido, porcentagem_lucro_liquido)

                return lucro_liquido
            except:
                pass
        
        resultado_janeiro = preencher_dre('Janeiro','Avj',valor_janeiro,despesa_janeiro)
        resultado_fevereiro = preencher_dre('Fevereiro','Avf',valor_fevereiro,despesa_fevereiro)
        resultado_marco = preencher_dre('Março','Avmç',valor_marco,despesa_marco)
        resultado_abril = preencher_dre('Abril','Avab',valor_abril,despesa_abril)
        resultado_maio = preencher_dre('Maio','Avmo',valor_maio,despesa_maio)
        resultado_junho = preencher_dre('Junho','Avjn',valor_junho,despesa_junho)
        resultado_julho = preencher_dre('Julho','Avjl',valor_julho,despesa_julho)
        resultado_agosto = preencher_dre('Agosto','Avag',valor_agosto,despesa_agosto)
        resultado_setembro = preencher_dre('Setembro','Avs',valor_setembro,despesa_setembro)
        resultado_outubro = preencher_dre('Outubro','Avo',valor_outubro,despesa_outubro)
        resultado_novembro = preencher_dre('Novembro','Avn',valor_novembro,despesa_novembro)
        resultado_desembro = preencher_dre('Dezembro','Avd',valor_dezembro,despesa_dezembro)

        return self.df
    
    def custos_fixos(self):
        #lista
        index = [
            'Pro Labore',
            'TI',
            'Site',
            'DNS',
            'Marketing',
            'Nuvem de arquivos'
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

        for cliente, i in enumerate(bd.custos_fixos_ler()):
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
                    for num, ince_linha_str in enumerate(linha_str):
                        #fazendo uma comparação se o indice encontrado ex "Produto" é igual ao valor que esta na lista ex "valor"
                        if linha_index == ince_linha_str:
                            nome = indice
                            descricao = linha_str[num+1]
                            #print(f'{nome}: {descricao}\n')
                            self.df.at[cliente,indice] = descricao
                    

if __name__ == '__main__':
    tr = tratamento_db()
    #tr.vendas()
    #tr.grafico_barra()
    #tr.cliente_s()
    #tr.planilha_completa()
    #tr.data_prazo()
    #tr.estoque_analise()
    #tr.dre()
    tr.custos_fixos()
    tr.salvar('custos_fixos.xlsx',)
    

    

    