_Python_

# Семинар 4

## Задача 4.1
Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

[Ссылка на dz4_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz4_1.py)

```sh
n = int(input("Количество знаков в Pi = "))

Pi = 0 
for i in range(n):
    Pi +=  1 / (16 ** i) * ( 4 / (8*i + 1) -  2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6))

print(f"{Pi:.{n}f}")
```
## Задача 4.2
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

[Ссылка на dz4_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz4_2.py)

```sh
n = int(input("Введите число: "))

def f(n, d=2):
    list_rez = []
    while d * d <= n:
        if n % d == 0:
            list_rez.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list_rez.append(n)
    return list_rez

print(n,"=", "*".join(map(str, f(n))))
```
## Задача 4.3
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

[Ссылка на dz4_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz4_3.py)

```sh
list1 = [12, 34, 34, 12, 55, 6, 4, 5, 77, 56, 34, 9, 231, 43]
list2 = []

# set(list1) 
# or
for i in list1:
    if i not in list2:
        list2.append(i)

print(list1, " -> ", list2)
```

# Семинар 3

## Задача 3.1
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

[Ссылка на dz3_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_1.py)

```sh
n = [2, 3, 5, 9, 3]
s = 0

for i in range(len(n)-1):
    if i % 2 != 0:
        s += n[i]

print(s)
```

## Задача 3.2
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

[Ссылка на dz3_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_2.py)

```sh
n = [2, 3, 4, 5, 6]

n_len = len(n)

if n_len % 2 == 0:
    n_len = n_len // 2
else:
    n_len = n_len // 2 + 1

for i in range(n_len):
    print(n[i] * n[len(n) - i - 1])
```

## Задача 3.3
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

[Ссылка на dz3_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_3.py)

```sh
n = [1.1, 1.2, 3.1, 5, 10.01] #=> 0.19
m = list()

for i in range(len(n)):
    j = float("0." + str(n[i] * 1.0).split(".")[1])
    if j != 0:
        m.append(j)

print(max(m) - min(m))
```
## Задача 3.5
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

[Ссылка на dz3_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_5.py)

```sh
list_fibo = list()
a0 = 0
a1 = 1
n = int(input())

for i in range(n + 1):
    list_fibo.append(a0)
    x = a0 + a1
    a0 = a1
    a1 = x

list_fibo2 = [list_fibo[i] * (-1) ** (i + 1) for i in range(len(list_fibo))][::-1]

print(list_fibo2 + list_fibo[1:])
```
## Задача 3.6
Сдвиг списка.

[Ссылка на dz3_6.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_6.py)

```sh
list_input = [1, 2, 3, 4, 5, 6, 7, 8]
list_output = list()

k = int(input("Сдвинуть на: "))

sliter = "(" + str(k) +")"
if k < 0 : 
    sliter = "<-- " + sliter
else:
    sliter = "--> " + sliter

k = k % len(list_input)

for i in range(len(list_input)):
   list_output.append(list_input[i-k])

print(list_input)
print(sliter)
print(list_output)
```

# Семинар 2

## Задача 2.1
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

[Ссылка на dz2_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_1.py)

```sh
n = int(input("Введите N (количество монеток): "))

reshka = 0
for i in range(n):
    drop = random.randint(0, 1)
    print(drop)
    if (drop):
        reshka +=1

print("---\n", min(reshka, n-reshka))
```

## Задача 2.2
Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

[Ссылка на dz2_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_2.py)

```sh
n = int(input("Введите N: "))
print(int(((1 + n) / 2) * n))
```

## Задача 2.3
Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

[Ссылка на dz2_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_3.py)

```sh
n = int(input("Введите N: "))

flag = True
i = 2

while flag:
    if n % i == 0:
        print(i)   
        flag = False
    i += 1
```

## Задача 2.4
Петя впервые пришел на урок физкультуры в новой школе.Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

[Ссылка на dz2_4.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_4.py)

```sh
n = int(input("Введите N: (кол-во учеников): "))

list_rost = list()

for i in range(n):
    list_rost.append(int(input(f"рост {i + 1} ученика: ")))

rost = int(input("Ваш рост: "))

list_rost.sort(reverse = True)

j = 1
for i in list_rost:
    print(i)
    if rost <= i:
        j += 1

print("---\n", j)
```
## Задача 2.5
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

[Ссылка на dz2_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_5.py)

```sh
n = int(input("Введите N: "))

arr = list()

for i in range(n):
    arr.append(int(input()))

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i-1] + arr[i] + arr[i+1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

print(max(arr_count))
```


# Семинар 1

## Задача 1.1
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

[Ссылка на dz1_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_1.py)

```sh
d = int(input("Введите день недели: "))

if d >= 1 and d <= 5:
    print("Рабочий день")
elif d == 6 or d == 7:
    print("Выходной день")
else: 
     print("День недели указывается от 1 до 7")
```

## Задача 1.2
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

[Ссылка на dz1_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_2.py)

```sh
print("X | Y | Z |  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z | (1) = (2) |   = ")
print("-------------------------------------------------------------")

for x in range(2):
    for y in range(2):
        for z in range(2):
            v1 = int(not (x or y or z))
            v2 = int(not x and not y and not z)
            print(f"{x} | {y} | {z} |  ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} |   {v1} = {v2}   |  {v1 == v2}")

print("-------------------------------------------------------------")
```

## Задача 1.3
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


[Ссылка на dz1_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_3.py)

```sh
x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))

rez = " четверти"
if x > 0 and y > 0:
    rez = "в" + str(1) + rez
elif  x < 0 and y > 0:
    rez = "в" + str(2) + rez
elif  x < 0 and y < 0:
    rez = "в" + str(3) + rez
elif  x > 0 and y < 0:
    rez = "в" + str(4) + rez
elif  x == 0 and y == 0:
    rez = "в нач6але координат"
else:
    rez = ("на плоскости")

print(f"точка находится {rez}")
```

## Задача 1.4
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


[Ссылка на dz1_4.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_4.py)

```sh
ch = int(input("Введите номер чертверти: "))

rez = "диапазон возможных координат "
if ch == 1:
    rez = rez + "Х ∈ [1, ∞] и Y ∈ [1, ∞]"
elif  ch == 2:
    rez = rez + "Х ∈ [-∞, -1] и Y ∈ [1, ∞]"
elif  ch == 3:
    rez = rez + "Х ∈ [-∞, -1] и Y ∈ [-∞, -1]"
elif  ch == 4:
    rez = rez + "Х ∈ [1, ∞] и Y ∈ [-1, -∞]"
else:
    rez = ("Необходимо ввести номер чертверти от 1 до 4")

print(rez)
```

## Задача 1.5
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


[Ссылка на dz1_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_5.py)

```sh
Ax, Ay = map(int, input("Введите координаты точки A(x, y), через пробел: ").split())
Bx, By = map(int, input("Введите координаты точки A(x, y), через пробел: ").split())

print("Расстояние между точками {:.2f}".format(((Bx - Ax) ** 2 + (By - Ay) ** 2) ** (0.5)))

```

## Задача 1.6
Числа Фибоначчи

[Ссылка на dz1_6.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_6.py)

```sh
f1 = 1
f2 = 1

n = 7  #input.txt
# или n = int(input("Введите N (0 ≤ N ≤ 30): "))

n -= 2
i = 0
while i < n:
    sum = f1 + f2
    f1 = f2
    f2 = sum
    i += 1
 
print("Число Фибоначчи:", f2) #OUTPUT.TXT
```