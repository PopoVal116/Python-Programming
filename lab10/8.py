shir=int(input('Введите ширину '))
dlin=int(input('Введите длину '))
s=0
for i in range(0, dlin):
    if i %2 ==0:
        print('#'*shir)
    else:
        if s%2==0:
            s+=1
            print("." * (shir - 1) + "#")
        else:
            s+=1
            print("#" + "." * (shir - 1))
