from posixpath import split
from random import *
t1=open('file8.txt', encoding='UTF8').readlines()
a=[]
for i in t1:
    s=i.split()
    if len(s[0]) >= 3:
        a.append(s[0])
n=randint(0, len(a)-1)
l=randint(0, len(a)-1)
while not (8 <= len(a[n]+a[l]) <= 10):
    n = randint(0, len(a)-1)
    l = randint(0, len(a)-1)
else:
    print(a[n]+a[l])
t1.close()
