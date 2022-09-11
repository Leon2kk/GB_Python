# Семинар 2.
# Задание № 3.

# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

import os
os.system('cls') # чистим консоль

n = int(input("Введите N: "))

flag = True
i = 2

while flag:
    if n % i == 0:
        print(i)   
        flag = False
    i += 1
    

