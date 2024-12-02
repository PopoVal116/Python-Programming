count=int(input('Введите количсетво человек на борту: '))
peopliki=[]
for i in range(0,count):
    peopliki.append(input('Введите человека: ').split(" "))
    peopliki[i][1]=peopliki[i][1].replace('woman','1').replace('captain','3').replace('man','2')\
        .replace('child','1')
for a,b in peopliki:
    if b=='1':
        print(a)
for a, b in peopliki:
    if b == '2':
        print(a)
for a, b in peopliki:
    if b == '3':
        print(a)
