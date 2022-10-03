
# Семинар 8.
# Задание № 1.

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

import os
os.system('cls') # чистим консоль

inputs = [1, 3, 3, 3, 4]

min = min(inputs)
max = max(inputs)

ouptuts = lambda x: [(min if i == max else i) for i in x]

print(inputs)
print(ouptuts(inputs))