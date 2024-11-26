import PySimpleGUI as sg
sg.theme("DarkPurple3")
layout = [[sg.Text('Бонжур! ты в игре "Эрудит", йоу. Сегодня ты узнаешь, смог бы \nстать крутым вожатым! Вводите с друзьями слова и узнайте у кого больше) '),  sg.InputText(key="niz", size=(20,2))],
 [sg.Image(filename='xomyak_zheka.png'), sg.Image(key='IMAGE') ],
 [sg.Button('Ща узнаем уровень крутости')],
 [sg.Text('Сумма очков крутости: '), sg.Text(key='output')]]
window = sg.Window('кто ты?', layout)
while 1:
    event, values = window.read()
    if event == 'Ща узнаем уровень крутости':
        slovarik = {'1': 'AEILNORSTU',
                    '2': 'DG',
                    '3': 'BCMP',
                    '4': 'FHVWY',
                    '5': 'K',
                    '8': 'JX',
                    '10': 'QZ'}
        shitalovo = 0
        slovo = values['niz'].upper()
        for bukva in slovo:
            for ball in slovarik:
                if bukva in slovarik[ball]:
                    shitalovo += int(ball)
        window['output'].update(shitalovo)
        window["IMAGE"].update(filename="kissa.png")
    if event == sg.WINDOW_CLOSED:
        break
window.close()
