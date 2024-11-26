import PySimpleGUI as sg
from random import *
sg.theme("DarkGreen")
layout = [[sg.Text('Введите диапозон зарплаты: ')],
 [sg.Text('Минимальная зпшка'), sg.InputText(key="niz")],
 [sg.Text('Mаксимальная зпшка'), sg.InputText(key="verx")],
 [sg.Button('Ща узнаем твою зепелю...')],
 [sg.Text('Зепелька равна'), sg.Text(key='output')],
 [sg.Image(key='IMAGE')] ]
window = sg.Window('Рандомчик зарплаты', layout)
while 1:
    event, values = window.read()
    if event == 'Ща узнаем твою зепелю...':
        niz = int(values['niz'])
        verx=int(values['verx'])
        if niz > verx:
            sg.popup_error('что-то напутали...')
        window['output'].update(randint(niz, verx))
        window["IMAGE"].update(filename="svinka.png")
    if event == sg.WINDOW_CLOSED:
        break
window.close()
