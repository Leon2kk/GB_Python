# Семинар 3.
# Задание № 5.

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import os
os.system('cls') # чистим консоль

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

