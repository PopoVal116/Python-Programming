#  Задание 1
# Необходимо реализовать метод трапеций для вычисления
# приближенного значения интеграла. Формула находится
# под рисунков. Шаг h вычисляется точно также как и в
# методе прямогульников.
# Выведите значения интегралов для N = 10, 100, 1000

'''def d(x):
    return x**2/(10+x**3)
a=-2
b=5
n=1000
h=(b-a)/n
f=[]
i=a
while i<b:
    f.append(d(i))
    i+=h
s=0
for j in range(0, len(f)-1):
    s+=h/2*(f[j]+f[j+1])
print(s)'''

# Задание 2
'''
from random import *

def f(a):
    if a[0][2]+a[1][2]+a[2][2]==a[0][1]+a[1][1]+a[2][1]==a[0][0]+a[1][0]+a[2][0]==a[0][0]+a[0][1]+a[0][2]==a[1][0]+a[1][1]+a[1][2]==a[2][0]+a[2][1]+a[2][2]==a[0][0]+a[1][1]+a[2][2]==a[0][2]+a[1][1]+a[2][0]==15:
        return True
    else:
        return False
def rand_square():
    rand,a= list(range(1, 10)),[]
    shuffle(rand)
    for i in range(0, 9, 3):
        a.append(rand[i:i + 3])
    return a
n = 3
a = rand_square()
while not(f(a)):
    a = rand_square()
else:
    print(a)
'''
# Задание 3
'''def distance(a,b):
    arr=[]
    for i in range(n):
        arr.append(((b[0][0] - a[i][0]) ** 2 + (b[0][1] - a[i][1]) ** 2)**0.5)
    for i in range(n):
        if arr[i] == min(arr):
            return a[i]

n=int(input('Введите количество сокровищ: '))
a=[[0]*2 for i in range(n)]
b=[[0]*2]
for i in range(n):
    for j in range(2):
        a[i][j] = int(input(f"Введите координату сокровища с позицией {i, j}: "))
        b[0][0]= int(input("Введите координату Сани с позицией (0,0): "))
        b[0][1] =int(input("Введите координату Сани с позицией (0,0): "))
        print(distance(a,b))
'''

# Задание 4
'''def new_dish(name,ing,price):
     menu.append([name,ing.split(','),int(price)])
menu = [["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]]
print('Введите число, обозначающее команду, которую хотите выполнить с меню(1, 2, 3, 4): ')
a = int(input())
if a == 1:
    print(menu)
elif a ==2:
    for i in range(len(menu)):
        if input("Какое блюдо вы хотите? ") == menu[i][0]:
            print(menu[i][1],menu[i][2])
elif a == 3:
    new_dish(input("Название нового блюда: "),input("Его ингридиенты: "),input("Прайс: "))
    print("Теперь меню выглядит так: ")
    print(menu)
elif a == 4:
    for i in range(len(menu)):
        if input("Цену на какое блюдо вы хотите изменить? ") == menu[i][0]:
            menu[i][2]=int(input("Введите новую цену: "))
            print("Теперь меню выглядит так: ")
            print(menu)
else:
    print('Ошибка')'''

# Задание 5
'''def input_matrix():
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    transposed = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed

if __name__ == "__main__":
    original_matrix = input_matrix()
    transposed_matrix = transpose_matrix(original_matrix)
    print("Транспонированная матрица:")
    for row in transposed_matrix:
        print(row)'''

# Задание 6
'''
def input_square_matrix(n):
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def swap_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    n = int(input("Введите размерность матрицы (n x n): "))
    matrix = input_square_matrix(n)
    swap_diagonals(matrix)
    print("Матрица после замены элементов на главной и побочной диагоналях:")
    print_matrix(matrix)'''

# Задание 7
'''from random import *
n=int(input("Кол-во рядов: "))
m=int(input("Кол-во мест: "))
matrix_1=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix_1[i][j] = randint(0, 1)
k=int(input("Введите количество билетов: "))
for l in range(n):
    print(matrix_1[l])
nulls_count=''
for i in range(n):
    for j in range(m):
        nulls_count+=''.join(str(matrix_1[i][j]))
    if "0"*k in nulls_count:
        print(f"Места есть, ближайший ряд {i+1}")
        break
else:
    print("Мест нет")'''

# Задание 8
'''
n,m=int(input("Введите количество строк: ")),int(input("Введите количество столбцов: "))
matrix=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[0][j] = 1
        matrix[i][0] = 1
        matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
for i in matrix:
    print(" ".join(f"{elem:6}" for elem in i))
'''