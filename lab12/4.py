import PySimpleGUI as sg
sg.theme('DarkPurple3')
def to_binary(n, bits=8):
    return bin(n & 0xFF)[2:].zfill(bits)
def to_ones_complement(n, bits=8):
    binary = to_binary(n, bits)
    ones_complement = "".join(['1' if bit == '0' else '0' for bit in binary])
    return ones_complement
def to_twos_complement(n, bits=8):
    binary = to_binary(n, bits)
    ones_complement = to_ones_complement(n, bits)
    twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(bits)
    return twos_complement
layout = [
    [sg.Text("Введите число от -128 до 127:")],
    [sg.Input(key="niz", size=(10, 1))],
    [sg.Button("Рассчитать")],
    [sg.Text("Прямой код:", size=(16, 1)), sg.Output(key="one", size=(10, 1))],
    [sg.Text("Обратный код:", size=(16, 1)), sg.Output(key="two", size=(10, 1))],
    [sg.Text("Дополнительный код:", size=(16, 1)), sg.Output(key="three", size=(10, 1))]
]
window = sg.Window("погнали", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Рассчитать":
        try:
            num = int(values["niz"])
            if -128 <= num <= 127:
                window["one"].update(to_binary(num))
                window["two"].update(to_ones_complement(num))
                window["three"].update(to_twos_complement(num))
            else:
                print("Число должно быть в диапазоне от -128 до 127.")
        except ValueError:
            print("Некорректный ввод. Введите целое число.")
window.close()
