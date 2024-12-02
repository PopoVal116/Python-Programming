import PySimpleGUI as sg
import random

pep, comp = 0, 0
count_matches = 0

compik = [[sg.Image("", key='computer_image')],
          [sg.Text("Ход компьютера")]]
peoplik = [[sg.Image("", key='player_image')],
           [sg.Text("Ход игрока")]]

vse = [[sg.Text('Счёт:'), sg.Text(f"{comp}:{pep}", key="score")],
       [sg.Text("Введите количество раундов"), sg.Input(key="count_matches", size=(20, 1))],
       [sg.Button('Установить раунды', key='set_matches')],
       [sg.Button('', image_filename='kamen).png', size=(15, 15), key='rock')],
       [sg.Button('', image_filename='bumaga.png', size=(10, 10), key='paper')],
       [sg.Button('', image_filename='noznis.png', size=(10, 10), key='scissors')]]

layout = [[sg.Column(compik), sg.VSeparator(), sg.Column(peoplik), sg.VSeparator(), sg.Column(vse, justification='right')]]

window = sg.Window("Камень, Ножницы, Бумага", layout)

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

    if event in ['rock', 'paper', 'scissors']:
        if count_matches <= 0:
            sg.popup("Игра окончена или не задано количество раундов. Установите количество раундов!")
            continue

        player_choice = event
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if player_choice == 'rock':
            window['player_image'].update(filename='kamen).png')
        elif player_choice == 'paper':
            window['player_image'].update(filename='bumaga.png')
        else:
            window['player_image'].update(filename='noznis.png')

        if computer_choice == 'rock':
            window['computer_image'].update(filename='kamen).png')
        elif computer_choice == 'paper':
            window['computer_image'].update(filename='bumaga.png')
        else:
            window['computer_image'].update(filename='noznis.png')

        if player_choice == computer_choice:
            result_text = "Ничья!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
            result_text = "Вы выиграли!"
            pep += 1
        else:
            result_text = "Вы проиграли!"
            comp += 1

        # Обновление счета
        window['score'].update(f"{comp}:{pep}")
        sg.popup(result_text)

        count_matches -= 1

        if count_matches == 0:
            sg.popup("Игра завершена!", f"Итоговый счёт: Компьютер {comp} : {pep} Игрок")
            pep, comp = 0, 0 
            window['score'].update(f"{comp}:{pep}")

window.close()