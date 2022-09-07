_Phyton_

# Семинар 1

## Задача 1
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

## Задача 2
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

## Задача 3
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

## Задача 4
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

## Задача 5
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


[Ссылка на dz1_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_5.py)

```sh
Ax, Ay = map(int, input("Введите координаты точки A(x, y), через пробел: ").split())
Bx, By = map(int, input("Введите координаты точки A(x, y), через пробел: ").split())

print("Расстояние между точками {:.2f}".format(((Bx - Ax) ** 2 + (By - Ay) ** 2) ** (0.5)))

```

## Задача 6
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