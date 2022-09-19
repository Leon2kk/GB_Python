# Семинар 4.
# Задание № 4.

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import os
os.system('cls') # чистим консоль

from random import randint as rd

k = int(input())

arr = list()
for i in range(k, 0, -1):
    x = rd(-100, 100)
    if x > 0 and i != k:
        arr.append(f'+{x}*x^{i}')
    else:
        arr.append(f'{x}*x^{i}')
        
x = rd(-100, 100)
if x > 0 and i != k:
    arr.append(f'+{x}')
else:
    arr.append(f'{x}')
arr.append(' = 0')
print(''.join(arr))
