import PySimpleGUI as sg

# Tema
sg.theme("DarkTeal")

# Layout
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar senha')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Loop de eventos
while True:
    eventos, valores = janela.read()
    
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Entrar':
        if valores['usuario'] == 'João' and valores['senha'] == '123456':
            print('Seja bem-vindo')
        else:
            print('Usuário ou senha inválidos')

janela.close()