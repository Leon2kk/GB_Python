# Семинар 1.
# Задание № 2.
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import os 
os.system('cls') # чистим консоль

print("X | Y | Z |  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z | (1) = (2) |   = ")
print("-------------------------------------------------------------")

for x in range(2):
    for y in range(2):
        for z in range(2):
            v1 = int(not (x or y or z))
            v2 = int(not x and not y and not z)
            print(f"{x} | {y} | {z} |  ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} |   {v1} = {v2}   |  {v1 == v2}")

print("-------------------------------------------------------------")