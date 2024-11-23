t=open('file6.txt', encoding='UTF8').readlines()
c=0
e=0
for i in t:
    s=i.split(' ')
    c+=len(s)
    e=i.count('e')
print(e*100/c)
t.close()