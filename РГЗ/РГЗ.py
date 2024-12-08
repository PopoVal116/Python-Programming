import PySimpleGUI as sg
import random

sg.theme("TanBlue")

pep, comp = 0, 0
count_matches = 0
peoplik_name=''

compik = [[sg.Image("", key='computer_image')],
          [sg.Text("Ход компьютера", justification='right')]]
peoplik = [[sg.Image("", key='player_image')],
           [sg.Text("Ход игрока", justification='right')]]

vse = [[sg.Text('Счёт:'), sg.Text(f"{comp}:{pep}", key="score")],
       [sg.Text('Игрок: '), sg.Input(key="name", size=(29, 1))],
       [sg.Text("Введите количество раундов"), sg.Input(key="count_matches", size=(10, 1))],
       [sg.Button('Установить раунды', key='set_matches')],
       [sg.Button('', image_filename='kamen).png', size=(30, 30), key='kamen')],
       [sg.Button('', image_filename='bumaga.png', size=(30, 30), key='bumaga')],
       [sg.Button('', image_filename='noznis.png', size=(30, 30), key='noznis')]]

layout = [[sg.Column(compik, size=(200, 200)), sg.VSeparator(), sg.Column(peoplik, size=(200, 200)), sg.VSeparator(), sg.Column(vse, justification='right')]]

window = sg.Window("Сыграешь?)", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'set_matches':
        try:
            count_matches = int(values['count_matches'])
            if count_matches <= 0:
                sg.popup("Пожалуйста, введите положительное число!")
                count_matches = 0
                continue
            sg.popup(f"Игра будет длиться {count_matches} раундов!")
        except ValueError:
            sg.popup("Пожалуйста, введите корректное число!")
            continue

    if event in ['kamen', 'bumaga', 'noznis']:
        if count_matches <= 0:
            sg.popup("Игра окончена или не задано количество раундов. Установите количество раундов!")
            continue

        player_choice = event
        computer_choice = random.choice(['kamen', 'bumaga', 'noznis'])

        if player_choice == 'kamen':
            window['player_image'].update(filename='kamen).png')
        elif player_choice == 'bumaga':
            window['player_image'].update(filename='bumaga.png')
        else:
            window['player_image'].update(filename='noznis.png')

        if computer_choice == 'kamen':
            window['computer_image'].update(filename='kamen).png')
        elif computer_choice == 'bumaga':
            window['computer_image'].update(filename='bumaga.png')
        else:
            window['computer_image'].update(filename='noznis.png')

        if player_choice == computer_choice:
            result_text = "Ничья!"
        elif (player_choice == 'kamen' and computer_choice == 'noznis') or (player_choice == 'bumaga' and computer_choice == 'kamen') or (player_choice == 'noznis' and computer_choice == 'bumaga'):
            result_text = "Вы выиграли!"
            pep += 1
        else:
            result_text = "Вы проиграли!"
            comp += 1

        peoplik_name=values['name']
        window['score'].update(f"{comp}:{pep}")
        sg.popup(result_text)

        count_matches -= 1

        if count_matches == 0:
            sg.popup("Игра завершена!", f"Итоговый счёт: Компьютер {comp} : {pep} {peoplik_name}")
            with open("kmngame.txt", "a") as f:
                f.write(f"{peoplik_name}: Компьютер {comp} : {pep} {peoplik_name}\n")
            pep, comp = 0, 0
            window['score'].update(f"{comp}:{pep}")

window.close()
