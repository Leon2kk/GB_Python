# Семинар 2.
# Задание № 2.

# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

import os
os.system('cls') # чистим консоль

n = int(input("Введите N: "))
print(int(((1 + n) / 2) * n))