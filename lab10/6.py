t=open('file5.txt', encoding='UTF8').readlines()
a=[]
for i in t:
    s=i.split()
    for x in s:
        print("".join(reversed(x)))
t.close()