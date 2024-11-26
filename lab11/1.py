alfovitik = {'1': '.,?:' ,
              '2' : 'ABC',
              '3' : 'DEF',
              '4' : 'GHI',
              '5' : 'JKL',
              '6' : 'MNO',
              '7': 'PQRS',
              '8' : 'TUV',
              '9' : 'WXYZ',
              '0' : ' '}
textik=input('Введите сообщение: ').upper()
for simvol in textik:
    for knopka in alfovitik:
        if simvol in alfovitik[knopka]:
            print(knopka*(alfovitik[knopka].index(simvol)+1), end='')



