# Семинар 3.
# Задание № 1.

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import os
os.system('cls') # чистим консоль

n = [2, 3, 5, 9, 3]
s = 0

for i in range(len(n)-1):
    if i % 2 != 0:
        s += n[i]

print(s)
