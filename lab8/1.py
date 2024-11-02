'''#   Задание 1
A=[]
x=input('Введите список данных: ')
A.append(x)
alf ='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
c='0123456789'
Z=[]
B=[]
for i in range(len(x)):
    if x[i] in alf:
        B.append(x[i])
    else:
        Z.append(x[i])
print(Z, B)'''
from random import random

'''#   Задание 2
import random
A=[]
c = 6
while c>0:
    i=random.randrange(49)
    A.append(i)
    c-=1
print(A)'''

'''#  Задание 3
c=[]
x =[1, 5, 2, 4, 3]
for i in range(len(x)-1):
    if x[i]<x[i+1]:
        c.append(x[i+1])
print(x)
print(c)'''

'''#  Задание 4
n = int(input("Введите количество элементов списка: "))
a = []
m=[]
b=[]
for i in range(0, n):
    elem = int(input("Введите элемент списка: "))
    a.append(elem)
avg = sum(a) / n
for j in range(len(a)):
    if a[j]<avg:
        m.append(a[j])
    else:
        b.append(a[j])
print(round(avg, 2))
print(m)
print(b)
'''

'''# Задание 5
n = int(input("Введите количество человек в строю: "))
a = []
m=[]
for i in range(0, n):
    elem = int(input("Введите рост человека: "))
    a.append(elem)
x = int(input('Введите рост Андрея: '))
for i in range(n):
    if x<=a[i]:
        m.append(i+2)
print(max(m))
'''

'''#   Задание 6
import random
a=[]
c=0
y=0
while y !=1:
    c +=1
    mon=random.choice(["O","P"])
    a.append(mon)
    for i in range(len(a)-2):
        if a[i]==a[i+1]==a[i+2]:
            y+=1
            print(a, c)
            break
'''

'''#  Заданеи 7
x = input('Введите номер карты: ')
c=0
n=0
for i in range(len(x)):
    if i % 2==0:
        if int(x[i])*2<=9:
            c+=(int(x[i])*2)
        else:
            c+=(int(x[i])*2)-9
    else:
        n+=int(x[i])
if (c+n) % 10 == 0:
    print('Корректный номер')
else:
    print('Некорректный номер')
'''

'''# Задание 8
a=[]
n = int(input('Введите количество слов: '))
for i in range(0, n):
    word=input('Введите слово: ')
    a.append(word)
for j in range(len(a)):
    s=a[j]
    print(s[0]+str((len(s)-2))+s[-1])
'''

'''# Задание 9
n=int(input('Введите количсетво комнат: '))
c=0
for i in range(0, n):
    p=int(input('Введите количество людей, которые уже живут в комнате: '))
    q=int(input('Введите максимальное количество человеек в комнате: '))
    if p<q:
        c+=1
print('Количество комнат, в которые могут заселиться Юра и Леша: ', c)
'''