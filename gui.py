import PySimpleGUI as sg
from datetime import date

data = date.today().year
ano = [data - i for i in range(5)]
selected_theme = 'Reddit'
sg.theme(selected_theme)

layout_login = [
    [sg.Stretch(),sg.Text('Nome',size=(8,1)),sg.Text('Ano',size=(5,1))],
    [sg.Stretch(),sg.Combo(['firefox','chrome','edge','internet']),sg.Combo([ano[0],ano[1],ano[2],ano[3],ano[4]])],
    [sg.Text('Nome',size=(13,1),justification='center'),sg.Text('E-mail',size=(13,1),justification='center'),
     sg.Text('Telefone',size=(13,1),justification='center'),sg.Text('Localidade',size=(10,1),justification='center')
     ],
    [sg.Input(size=(16,1)),sg.Input(size=(16,1)),
     sg.Input(size=(11,1)),sg.Input(size=(11,1))
     ],
     [sg.Text('Descricao',size=(13,1),justification='center'),sg.Text('Quantidade',size=(13,1),justification='center'),
     sg.Text('Valor',size=(13,1),justification='center'),sg.Text('Data venda',size=(10,1),justification='center')
     ],
    [sg.Input(size=(16,1)),sg.Input(size=(16,1)),
     sg.Input(size=(11,1)),sg.Input(size=(11,1))
     ],
     [sg.Text('Uber flash',size=(13,1),justification='center'),sg.Text('Impressao',size=(13,1),justification='center'),
     sg.Text('Outros',size=(13,1),justification='center')
     ],
    [sg.Input(size=(16,1)),sg.Input(size=(16,1)),
     sg.Input(size=(11,1)),sg.Button('Excel',size=(9,1))
     ],
     [sg.Button('Inserir',size=(10,1)),sg.Button('Atualizar',size=(10,1)),sg.Button('Deletar',size=(10,1))]
    ]

window = sg.Window('Myframe', icon='favicon.ico',layout=layout_login, keep_on_top=True, finalize = True)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
        break

window.close()