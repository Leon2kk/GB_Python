# Семинар 3.
# Задание № 6.

# Сдвиг списка.

import os
os.system('cls') # чистим консоль

list_input = [1, 2, 3, 4, 5, 6, 7, 8]
list_output = list()


k = int(input("Сдвинуть на: "))

sliter = "(" + str(k) +")"
if k < 0 : 
    sliter = "<-- " + sliter
else:
    sliter = "--> " + sliter

k = k % len(list_input)

for i in range(len(list_input)):
   list_output.append(list_input[i-k])


print(list_input)
print(sliter)
print(list_output)
