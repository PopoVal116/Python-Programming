t=open('file7.txt', encoding='UTF8').readlines()
stroka=input('Напиши что-то доброе ')
n=len(t)//2
print(*t[:n], stroka, *t[n:])
t.close()