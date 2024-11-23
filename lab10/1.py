t=open('file4.txt', encoding='UTF8').readlines()
b=[]
for i in t:
    peoplik=i.split()
    b.append(peoplik[-1])
b[b.index(max(b))]='-10'
print(t[b.index(max(b))])
t.close()