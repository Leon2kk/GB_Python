# Семинар 1.
# Задание № 6.

# Числа Фибоначчи

import os 
os.system('cls') # чистим консоль

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