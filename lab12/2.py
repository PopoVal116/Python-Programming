len=int(input('Введите количество сообщений '))
messeges=input()
if messeges[0]=='Q' and (messeges.count('Q')==messeges.count('A')) and messeges[-1]!='Q':
    print('+')
else:
    print('-')
