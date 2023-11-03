import pandas as pd

df = pd.read_excel('VENDA 2023.xlsx')
print(df)

estoque_2023= [
    'BRANDÃO MOLDURAS,20X25,5,78,23/11/2022',
    'BRANDÃO MOLDURAS, 15X21,3, 48.46, 23/11/2022',
    'OLIVEIRA MOLDURAS S/A, 29.7 x 42  (A3), 1,65, 31/08/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,20,500,08/08/2023',
    'OLIVEIRA MOLDURAS S/A,15X21,10,200,08/08/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,2,50,23/01/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,2,50,31/01/2023',
    'BRANDÃO MOLDURAS,20X25,5,190.37,21/02/2023',
    'BRANDÃO MOLDURAS,15X21,10,149.57,22/02/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,1,25,05/04/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,1,25,20/04/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,5,125,09/05/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,1,25,09/05/2023',
    'MOLDURAS PEREIRA,20X25,10,146.1,04/05/2023',
    'PMG PRINT,SACOLA PAPEL G,20,65.01,25/05/2023',
    'PMG PRINT,SACOLA PAPEL M,10,27.4,25/05/2023',
    'RIZE SHOPE,FIO DE FADA,10,51.17,25/05/2023',
    'BRANDÃO MOLDURAS,20X25,12,237.17,29/05/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,1,25,16/05/2023',
    'OLIVEIRA MOLDURAS S/A,20X25,4,100,20/07/2023',
    'PD MOLDURAS,PENDURADOR,20,17.75,22/08/2023'
]
venda_2023 = [
'PAMELA AZIZ,@gmail.com,00 990000000,campo grande,DIAS DOS PAIS 15X21 - Preto,1,50,08-12-yyyy,0,0,0,Concluido',
'KELI FARIAS ,@gmail.com,00 990000001,campo grande,15X21 - Preto,1,50,08-13-yyyy,0,0,0,Concluido',
'DIEGO ROBLES,@gmail.com,00 990000002,campo grande,15X21 - Preto,1,50,08-19-yyyy,4.53,0,0,Concluido',
'PATRICIA EMYLLI,@gmail.com,00 990000003,campo grande,20X25,1,65,08-10-yyyy,0,0,0,Concluido',
'RAIANE,@gmail.com,00 990000004,campo grande,20X25,1,65,08-10-yyyy,0,0,0,Concluido',
'ANA LELIS,@gmail.com,00 990000005,campo grande,20X25,1,65,08-12-yyyy,0,0,0,Concluido',
'UYARA,@gmail.com,00 990000006,campo grande,20X25 - Branco,1,66.91,08-11-yyyy,0,0,0,Concluido',
'PATRICIA EMYLLI,@gmail.com,00 990000007,campo grande,20X25 - Branco,1,65.34,08-12-yyyy,0,0,0,Concluido',
'HELENA,@gmail.com,00 990000008,campo grande,20X25 - Preto,1,65,08-11-yyyy,0.26,0,0,Concluido',
'SHIRLEY,@gmail.com,00 990000009,campo grande,20X25 - Preto,1,65,09-11-yyyy,0,0,0,Concluido',
'PAULA RISSI,@gmail.com,00 990000010,campo grande,BEST 8 20X25 - BRANCO,1,65,06-17-yyyy,0,0,0,Concluido',
'Lorrayne Nicolosi - ELO7,@gmail.com,00 990000011,campo grande,BEST 8 20X25 - PRETO,1,53.3,02-08-yyyy,0,0,0,Concluido',
'MICAELY SALES - ELO7,@gmail.com,00 990000012,campo grande,BEST 8 20X25 - PRETO,1,53.3,02-12-yyyy,0,0,0,Concluido',
'Jade Perez - ELO7,@gmail.com,00 990000013,campo grande,BEST 8 20X25 - PRETO,1,53.3,03-27-yyyy,0,0,0,Concluido',
'Amanda Karen Schittkowski - ELO7,@gmail.com,00 990000014,campo grande,BEST 8 20X25 - PRETO,1,53.3,05-10-yyyy,0,0,0,Concluido',
'Bárbara Sparapan - ELO7,@gmail.com,00 990000015,campo grande,BEST 8 20X25 - PRETO,1,53.3,07-17-yyyy,0,0,0,Concluido',
'Camilla Roque Calvano Pavão - ELO7,@gmail.com,00 990000016,campo grande,BEST 8 20X25 - PRETO,1,53.3,08-18-yyyy,0,0,0,Concluido',
'VINICIUS DE MORAES,@gmail.com,00 990000017,campo grande,BEST 8 20X25 PRETO,1,80,05-12-yyyy,0,0,0,Concluido',
'Tânia Valéria Tasca - ELO7,@gmail.com,00 990000018,campo grande,CASAMENTO 20x25 - Branco,1,53.3,01-06-yyyy,0,0,0,Concluido',
'Rita Gorete - ELO7,@gmail.com,00 990000019,campo grande,CASAMENTO 20x25 - Branco,1,53.3,01-25-yyyy,0,0,0,Concluido',
'Rafaela Cabral Ferreira Araújo - ELO7,@gmail.com,00 990000020,campo grande,CASAMENTO 20x25 - Branco,1,53.3,04-18-yyyy,0,0,0,Concluido',
'Fabricio Moreira Reis - ELO7,@gmail.com,00 990000021,campo grande,CASAMENTO 20x25 - Branco,1,53.3,05-26-yyyy,0,0,0,Concluido',
'Ana Carolina Martins - ELO7,@gmail.com,00 990000022,campo grande,CASAMENTO 20x25 - Branco,1,53.3,07-05-yyyy,0,0,0,Concluido',
'RAMON DE MELO DE SOUZA - ELO7,@gmail.com,00 990000023,campo grande,CASAMENTO 20x25 - Branco,1,53.3,07-08-yyyy,0,0,0,Concluido',
'Oscar Baptista dos Santos - ELO7,@gmail.com,00 990000024,campo grande,CASAMENTO 20x25 - Branco,1,53.3,07-10-yyyy,0,0,0,Concluido',
'MARIUCHA - ELO7,@gmail.com,00 990000025,campo grande,CASAMENTO 20x25 - Branco,1,53.3,09-07-yyyy,0,0,0,Concluido',
'GABRIELLY - ELO7,@gmail.com,00 990000026,campo grande,CASAMENTO 20x25 - Branco,1,53.3,09-12-yyyy,0,0,0,Concluido',
'BIA CLIENTE,@gmail.com,00 990000027,campo grande,CHAVEIRO + POLAROID,1,8,09-11-yyyy,0,0,0,Concluido',
'Dalete Queiroz de Jesus - ELO7,@gmail.com,00 990000028,campo grande,CORAÇÃO 20X25 - PRETO,1,53.3,08-22-yyyy,0,0,0,Concluido',
'GABRIEL ÂNGELO - ELO7,@gmail.com,00 990000029,campo grande,DATA 20X25 - Branco,1,53.3,01-01-yyyy,0,0,0,Concluido',
'Edson Costa Junior - ELO7,@gmail.com,00 990000030,campo grande,DATA 20X25 - Branco,1,53.3,03-13-yyyy,0,0,0,Concluido',
'Alice Watson Cleto - ELO7,@gmail.com,00 990000031,campo grande,DATA 20X25 - Branco,1,53.3,03-19-yyyy,0,0,0,Concluido',
'Rosane - ELO7,@gmail.com,00 990000032,campo grande,DATA 20X25 - Branco,1,53.3,05-02-yyyy,0,0,0,Concluido',
'Priscila Demarchi - ELO7,@gmail.com,00 990000033,campo grande,DATA 20X25 - Branco,1,53.3,08-23-yyyy,0,0,0,Concluido',
'Pedro Augusto Silva de Oliveira,@gmail.com,00 990000034,campo grande,DATA 20X25 - PRETO,1,53.3,02-01-yyyy,0,0,0,Concluido',
'Taylon Roger Souza Santos - ELO7,@gmail.com,00 990000035,campo grande,DATA 20X25 - PRETO,1,53.3,08-06-yyyy,0,0,0,Concluido',
'RAYLLA,@gmail.com,00 990000036,campo grande,ESTRELAS 15X21 PRETO,1,50,01-31-yyyy,0,0,0,Concluido',
'Igor Amaral - ELO7,@gmail.com,00 990000037,campo grande,ESTRELAS 20X25 - PRETO,1,53.3,01-17-yyyy,0,0,0,Concluido',
'Kauana Caetano - ELO7,@gmail.com,00 990000038,campo grande,ESTRELAS 20X25 - PRETO,1,53.3,02-25-yyyy,0,0,0,Concluido',
'Priscilla Stallbaum,@gmail.com,00 990000039,campo grande,FAMILIA 20X25 PINUS,2,115,05-08-yyyy,0,0,0,Concluido',
'AUXILIADORA ,@gmail.com,00 990000040,campo grande,FOTO 20X25 PRETO,2,138,05-12-yyyy,0,0,0,Concluido',
'Priscilla Stallbaum,@gmail.com,00 990000041,campo grande,IMPRESSÃO FOTOS,2,29,07-19-yyyy,0,0,0,Concluido',
'LARA CLIENTE,@gmail.com,00 990000042,campo grande,KIT POLAROID C/ LUZ,1,45,08-30-yyyy,0,0,0,Concluido',
'Vinícius Rangel - ELO7,@gmail.com,00 990000043,campo grande,KIT POLAROID S/ LUZ,1,53.3,05-17-yyyy,0,0,0,Concluido',
'JULIA,@gmail.com,00 990000044,campo grande,KIT POLAROID S/ LUZ,1,35,09-08-yyyy,0,0,0,Concluido',
'BEATRIZ DUARTE,@gmail.com,00 990000045,campo grande,MÃE 20X25 BRANCO,1,50,05-12-yyyy,0,0,0,Concluido',
'JOYCE MIGUEL,@gmail.com,00 990000046,campo grande,NASCIMENTO 20X25,1,60,08-10-yyyy,0,0,0,Concluido',
'NADINE,@gmail.com,00 990000047,campo grande,NASCIMENTO 20X25 - Branco,1,53.3,09-13-yyyy,0,0,0,Concluido',
'EVERSON ,@gmail.com,00 990000048,campo grande,NASCIMENTO 20X25 - BRANCO / MÃE CORAÇÃO 20X25 BRANCO,2,130,05-12-yyyy,0,0,0,Concluido',
'JOYCE MIGUEL,@gmail.com,00 990000049,campo grande,PARA O MELHOR 15X21 - Preto / Nascimento 20X25 - Branco,2,115,09-03-yyyy,0,0,0,Concluido',
'Jheniffer  Xenxen,@gmail.com,00 990000050,campo grande,POLAROID,1,8,06-11-yyyy,0,0,0,Concluido',
'WEILA,@gmail.com,00 990000051,campo grande,POLAROID,1,23,06-12-yyyy,0,0,0,Concluido',
'REBECA BRASIL,@gmail.com,00 990000052,campo grande,POLAROID,1,5.5,08-18-yyyy,0,0,0,Concluido',
'BARBARA,@gmail.com,00 990000053,campo grande,POLAROID,1,10,08-19-yyyy,0,0,0,Concluido',
'HANNAH,@gmail.com,00 990000054,campo grande,POLAROID,6,45,09-08-yyyy,0,0,0,Concluido',
'ANA CRISTINA,@gmail.com,00 990000055,campo grande,QUADRO 29.7 x 42  (A3),1,100,08-31-yyyy,0,0,0,Concluido',
'THAMI FERREIRA,@gmail.com,00 990000056,campo grande,QUADRO MOSAICO 8 FOTOS 20x25 - Preto,1,50,09-06-yyyy,5.96,0,0,Concluido',
'LAIS DIEGUES,@gmail.com,00 990000057,campo grande,QUADRO VARAL 15X21 PRETO,1,50,05-13-yyyy,0,0,0,Concluido',
'ANDREZA,@gmail.com,00 990000058,campo grande,QUADRO VARAL 20X25 - PRETO,1,60,06-05-yyyy,0,0,0,Concluido',
'FRANCINALICE (Bia Cliente),@gmail.com,00 990000059,campo grande,Ser Pai 20X25 - Preto / CHAVEIRO,1,73,08-12-yyyy,0,0,0,Concluido',
'Ingrid Melissa Alves de Lima - ELO7,@gmail.com,00 990000060,campo grande,SPOTIFY 15X21 - PRETO,2,82,06-15-yyyy,0,0,0,Concluido',
'GABRIELLY,@gmail.com,00 990000061,campo grande,SPOTIFY 15X21 - Preto,1,50,09-12-yyyy,0,0,0,Concluido',
'GUSTAVO MAGALHÃES,@gmail.com,00 990000062,campo grande,Spotify 15X21 - Preto / POSTER ,2,74.5,09-05-yyyy,11.28,0,0,Concluido',
'ANA LINO,@gmail.com,00 990000063,campo grande,SPOTIFY 15X21 - PRETO.,1,50,05-22-yyyy,0,0,0,Concluido',
'CAMILA 2 CLIENTE,@gmail.com,00 990000064,campo grande,SPOTIFY 15X21 PRETO / VARAL 15X21 /  4 FOTOS POLAROID,6,116,05-06-yyyy,0,0,0,Concluido',
'BRUNO OLIVEIRA,@gmail.com,00 990000065,campo grande,SPOTIFY 20X25 - Branco,1,65,09-11-yyyy,9.35,0,0,Concluido',
'LUCAS BRASIL,@gmail.com,00 990000066,campo grande,SPOTIFY 20X25 - PRETO,1,65,05-30-yyyy,0,0,0,Concluido',
'IRENE,@gmail.com,00 990000067,campo grande,,1,60,01-10-yyyy,0,0,0,Concluido',
'ANDREZA,@gmail.com,00 990000068,campo grande,,1,70,01-12-yyyy,0,0,0,Concluido',
'MARIA RITA,@gmail.com,00 990000069,campo grande,,1,30,01-23-yyyy,0,0,0,Concluido',
'THAIS MARIA,@gmail.com,00 990000070,campo grande,,1,30,02-03-yyyy,0,0,0,Concluido',
'KAREN CHRISTINA,@gmail.com,00 990000071,campo grande,,1,73,02-04-yyyy,0,0,0,Concluido',
'TAIARA BUFFARO,@gmail.com,00 990000072,campo grande,,1,39,02-06-yyyy,0,0,0,Concluido',
'GREICY,@gmail.com,00 990000073,campo grande,,1,6.75,02-10-yyyy,0,0,0,Concluido',
'YEISON GABRIEL,@gmail.com,00 990000074,campo grande,,1,60,02-17-yyyy,0,0,0,Concluido',
'LE,@gmail.com,00 990000075,campo grande,,1,35,02-27-yyyy,0,0,0,Concluido',
'PATRICK DIOGO,@gmail.com,00 990000076,campo grande,,1,60,03-02-yyyy,0,0,0,Concluido',
'IRENE,@gmail.com,00 990000077,campo grande,,1,60,03-06-yyyy,0,0,0,Concluido',
'WENDEL,@gmail.com,00 990000078,campo grande,,1,14,04-22-yyyy,0,0,0,Concluido',
'MARCELA LOPES,@gmail.com,00 990000079,campo grande,,1,64,05-11-yyyy,0,0,0,Concluido',
'NATALIA MOREIRA,@gmail.com,00 990000080,campo grande,,1,72.05,05-12-yyyy,0,0,0,Concluido',
'MARCOS CESAR,@gmail.com,00 990000081,campo grande,,1,65,05-13-yyyy,0,0,0,Concluido',
'KAMILA MARTINS,@gmail.com,00 990000082,campo grande,,2,120.5,05-13-yyyy,0,0,0,Concluido',
'DENYSE DONEGA,@gmail.com,00 990000083,campo grande,,1,71,06-02-yyyy,0,0,0,Concluido',
'LORENA MICHELINI,@gmail.com,00 990000084,campo grande,,1,62,06-03-yyyy,0,0,0,Concluido',
'GEOVANNA SILVA,@gmail.com,00 990000085,campo grande,,1,60,06-09-yyyy,0,0,0,Concluido',
'Pedro Augusto,@gmail.com,00 990000086,campo grande,,1,65,06-10-yyyy,0,0,0,Concluido',
'ANA BEATRIZ ,@gmail.com,00 990000087,campo grande,,1,6.5,06-10-yyyy,0,0,0,Concluido',
'Cinthya Duarte,@gmail.com,00 990000088,campo grande,,1,65,06-12-yyyy,0,0,0,Concluido',
'KALINNY,@gmail.com,00 990000089,campo grande,,1,79,06-12-yyyy,0,0,0,Concluido',
'DAINÁ,@gmail.com,00 990000090,campo grande,,1,80,06-15-yyyy,0,0,0,Concluido',
'BEATRIZ DUARTE,@gmail.com,00 990000091,campo grande,,1,16,06-20-yyyy,0,0,0,Concluido',
'ELTON MOREL,@gmail.com,00 990000092,campo grande,,1,35,07-05-yyyy,0,0,0,Concluido',
'DENYSE DONEGA,@gmail.com,00 990000093,campo grande,,1,56,07-21-yyyy,0,0,0,Concluido',
'PEDRO BEZERRA,@gmail.com,00 990000094,campo grande,,1,50,07-25-yyyy,0,0,0,Concluido',
'NETO,@gmail.com,00 990000095,campo grande,,1,65,09-18-yyyy,0,0,0,Concluido',
'THAIS ELO7,@gmail.com,00 990000096,campo grande,quadro data 20x25 branco,1,53.3,09-21-yyyy,0,0,0,Concluido',
'bryan elo 7,@gmail.com,00 990000097,campo grande,quadro casamento 20x25 branco,1,53.30,09-26-yyyy,0,0,0,Concluido',
'paloma elo7,@gmail.com,00 990000098,campo grande,quadro amor 20x25 preto,1,53.30,09-26-yyyy,0,0,0,Concluido',
'jessica elo7,@gmail.com,00 990000099,campo grande,quadro data a3 branco,1,93.30,09-27-yyyy,0,0,0,Concluido',
'LUCAS ELO7,@gmail.com,00 990000100,campo grande,VARAL + QUADRO DATA 20X25 BRANCO,2,108,02-10-yyyy,0,0,0,Concluido',
]

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

