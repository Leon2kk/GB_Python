# Семинар 1.
# Задание № 4.
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import os 
os.system('cls') # чистим консоль

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
