t=open('file7.txt', encoding='UTF8').readlines()
t1=open('file8.txt', encoding='UTF8').readlines()
a=[]
b=[]
for i in t1:
    peoplikmen=i.split()
    a.append(peoplikmen[0])
for j in t:
    peoplikwomen=j.split()
    b.append(peoplikwomen[0])
n=int(input('Введи число пожалуйста:) '))
peoplikpol=input('Введите пол пеоплика: ')
if peoplikpol == 'м':
    print(*a[:n])
if peoplikpol == 'ж':
    print(*b[:n])
t.close()
t1.close()