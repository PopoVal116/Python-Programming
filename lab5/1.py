'''#                       №1
#Напишите программу, в которой пользователь
# сможет ввести временной промежуток в виде
# количества дней, часов, минут и секунд и узнать
# общее количество секунд, составляющее введенный
#отрезок.
print("Введите временной промежуток(число):")
d = int(input("Дни:"))
h = int(input("Часы:"))
m = int(input("Минуты:"))
s = int(input("Секунды:"))
rez = (d * 86400)+(h*3600)+(m*60)+s
print("Общее количество секунд, составляющее введенный отрезок:", rez)
'''

'''
#                        №2
#Вводится число N, необходимо отрезать от него K
# последних цифр (Вспомнить об % (остаток от
# деления))

N = int(input("Введите число:"))
K = int(input("Введите число, означающее количество отрезанных цифр:"))
rez = N % (10**K)
print(rez)
'''

'''
#                        №3
#Дано трехзначное число. Найдите сумму его цифр
a = int(input("Введите трехзначное чило:"))
sum = 0
while a > 0:
    sum = sum + (a % 10)
    a = a // 10
print("Сумма цифр числа:", sum)
'''


#                          №4
x = int(input("""Вы находитесь в землях, заселенных драконами. Перед собой вы видите две пещеры. В одной
из них — дружелюбный дракон, который готов поделиться с вами своими сокровищами. Во второй
— жадный и голодный дракон, который мигом вас съест. В какую пещеру вы войдете? (нажмите
клавишу 1 или 2)
"""))
print("""Вы приближаетесь к пещере...
Ее темнота заставляет вас дрожать от страха...
Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...""")
s = str(input("ДА или НЕТ"))
if s == "ДА" or s == "да":
    print("...делится с вами своими сокровищами")
elif s == "НЕТ" or s == "нет":
    print("...моментально вас съедает!")
else:
    print("EROR")


'''
#                    №5
#Все треугольники могут быть отнесены к тому или
# иному классу (равнобедренные, равносторонние и
# разносторонние) на основании длин их сторон.
# Равносторонний треугольник характеризуется
#одинаковой длиной всех трех сторон, равнобедренный
# – двух сторон из трех, а у разностороннего
#треугольника все стороны разной длины.
#Напишите программу, которая будет запрашивать у
# пользователя длины всех трех сторон треугольника
# и выдавать сообщение о том, к какому типу следует
# его относить

print("Введите длины сторон треугольника:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if ((a + b) <= c) or ((a + c) <= b) or ((b +c) <= a):
    print("Это не треугольник...")
elif a == b ==c:
    print("равносторонний")
elif a == b or a == c or b ==c:
    print("рфвнобедренный")
else:
    print("разносторонний")
 '''

'''
#                 №6
#Количество дней в месяце варьируется от 28 до 31.
# Очередная ваша программа должна запрашивать у
# пользователя название месяца и отображать
# количество дней в нем. Поскольку года мы не
#учитываем, для февраля можно вывести сообщение о
# том, что этот месяц может состоять как из 28,
#так и из 29 дней, чтобы учесть фактор високосного
# года.
m = str(input("Введите название месяца(с большой буквы без пробела):"))
if m == "Февраль":
    print("этот месяц может состоять как из 28, так и из 29 дней")
elif m == "Январь" or m == "Март" or m == "Июль" or m == "Август" or m == "Октябрь" or m == "Декабрь" or m == "Май":
    print("31 день")
else:
    print("30 дней")'''