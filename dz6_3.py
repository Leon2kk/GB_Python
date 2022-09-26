# Семинар 6.
# Задание № 3.

# Парам пам-пам Пам парам

import os
os.system('cls') # чистим консоль

fraza = "пара-ра-рам рам-пам-папам па-ра-па-дам".split()

rez = [sum(x in 'ауоиэыяюеё' for x in i) for i in fraza]

if len(set(rez)) == 1: # именно == 1
    print("Парам пам-пам") 
else: 
    print("Пам парам")
