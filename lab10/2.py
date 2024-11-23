t=open('file5.txt', encoding='UTF8').readlines()
t1=open('file6.txt', encoding='UTF8').readlines()
for i in t:
    if 'Academy' in i:
        print('В 5 файле')
        break
else:
    print('В 6 файле')
t.close()
t1.close()