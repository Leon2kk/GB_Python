# Семинар 4.
# Задание № 2.

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls') # чистим консоль

# 600 = 2*2*2*3*5*5
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

