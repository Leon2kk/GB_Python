_Python_

# Семинар 9

## Задача 9.1
Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)
Создайте программу для игры с конфетами человек против бота(интелект). (Дополнительно)
Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования(Дополнительно)

[Ссылка на dz9\bot.py](https://github.com/Leon2kk/GB_Python/blob/master/dz9/bot.py)

```sh
# В консоле выполняем команду
# pip install pytelegrambotapi

import telebot;
bot = telebot.TeleBot('удалено')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    message_list = message.text.split()
    message_result = list()

    for item in message_list:
        if 'абв' not in item:
            message_result.append(item)
    
    bot.send_message(message.from_user.id,  " ".join(message_result))
    
bot.polling(none_stop=True, interval=0)
```
### Ркзультат
![Ссылка на dz9\screen.jpg](https://github.com/Leon2kk/GB_Python/blob/master/dz9/screen.jpg)


# Семинар 8

## Задача 8.1
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

[Ссылка на dz8_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz8_1.py)

```sh
inputs = [1, 3, 3, 3, 4]

min = min(inputs)
max = max(inputs)

ouptuts = lambda x: [(min if i == max else i) for i in x]

print(ouptuts(inputs))
```

## Задача 8.2
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). Через рекурсию необходимо делать

[Ссылка на dz8_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz8_2.py)

```sh
inputs = [1, 2, 3, 4, 5, 12]

def reverses(inp, i):
    if i >= 0: 
        print(inp[i], end=' ')      
        i -= 1
        reverses(inp, i)
       
reverses(inputs, len(inputs)-1)
```

# Семинар 7

## Задача 7.1
Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных формате .txt.
Дополнительно сделать в нескольких форматах(.json, .csv, .xlsx..)

[Ссылка на файлы dz7](https://github.com/Leon2kk/GB_Python/blob/master/dz7/)

# Семинар 6

## Задача 6.1
Мимикрия

[Ссылка на dz6_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz6_1.py)

```sh
transfomation = lambda x: x

values = [1, 2, 3, 5, "abc"]
transformed_values = list(map(transfomation, values))

if values == transformed_values:
    print("ok")
else:
    print("fail")
```

## Задача 6.2
Самая далёкая планета

[Ссылка на dz6_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz6_2.py)

```sh
def find_farthest_orbit(orbits):
    return  max(orbits, key=lambda x: 3.14159 * x[0] * x[1] if (x[0] != x[1]) else False)

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
```

## Задача 6.3
Парам пам-пам Пам парам

[Ссылка на dz6_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz6_3.py)

```sh
fraza = "пара-ра-рам рам-пам-папам па-ра-па-дам".split()

rez = [sum(x in 'ауоиэыяюеё' for x in i) for i in fraza]

if len(set(rez)) == 1: # именно == 1
    print("Парам пам-пам") 
else: 
    print("Пам парам")
```

## Задача 6.4
Все равны, как на подбор

[Ссылка на dz6_4.py](https://github.com/Leon2kk/GB_Python/blob/master/dz6_4.py)

```sh
characteristic = lambda x: x

def same_by(characteristic, objects):    
    if len(set(characteristic(i) for i in objects)) == 1 or not objects:
        return True
    else:
        return False

values = [0, 2, 4, 6, 8, 10]

if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
```

## Задача 6.5
Таблица мат.операции

[Ссылка на dz6_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz6_5.py)

```sh
def print_operation_table(operation, rows = 9, cols = 9):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(operation(i, j), end='\t')
        print()            

print_operation_table(lambda x, y: x * y, 5)
```

# Семинар 5

## Задача 5.1
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

[Ссылка на dz5_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz5_1.py)

```sh
money = 2021
max_money_step = 28
bank = 0

player1 = "1 игрок"
player2 = "2 игрок"
players = [player1, player2]

def toEndGame(pl):
    print(f'Игра окончена, {pl} выйграл!')

def toGame(count_money):
    while(count_money > 0):
        for i in players:
            if count_money > 0:
                print(f'Осталось {count_money} конфет')
                
                if (count_money < max_money_step):
                    bank = count_money
                else:
                    bank = max_money_step

                step = int(input(f'{i} выберите от 1 до {bank} конфет: '))
                if step < 1 or step > bank:
                    print(f'Вы ввели {step}, а надо от 1 до {bank}, пропускаете ход')
                    continue
                else:
                    count_money -= step
            else:
                return i
        if count_money <= 0:
           toEndGame(i)

toGame(money)
```
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""

[Ссылка на dz5_1a.py](https://github.com/Leon2kk/GB_Python/blob/master/dz5_1a.py)

```sh
from random import randint, choice

print('DZ / 5 / 1(a, b) Игра в конфетки')

msg = ['Ваша очередь',
        'берите конфеты',
        'сколько возьмёте?',
        'берите',
        'ваш ход']


def introduce_players():
    player1 = input('Как вас зовут?\n')
    player2 = 'Т-800'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = randint(0, 1)
    if first == 1:
        print(f"Жеребёка определила что вы {players[0]} ходите первым!")
    else:
         print(f"Жеребёка определила что я {players[1]} хожу первым!")
    return [n, m, int(first)]


def play_game(rules, players, msg):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'-> Взято {move}')
        else:
            print(f'{players[0]}, {choice(msg)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Не верно указано, не более {rules[1]} конфет{letter}, всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Не верно указано, за мухлёж игра окончена')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, msg)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Последний кто выбрал {winer}, - побеждает!')
```
## Задача 5.2
Создайте программу для игры в ""Крестики-нолики"".

[Ссылка на dz5_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz5_2.py)

```sh
import tkinter as tk
from tkinter import messagebox as mb
import random as rnd

window = tk.Tk() 
window.title("GB / 5-2 / Крестики-нолики")

pole = [None] * 9
btn_num_clicked = list(range(9))
step = 0

def is_win(player):
    if (pole[0] == pole[1] == pole[2] == player) or (pole[3] == pole[4] == pole[5] == player) or (pole[6] == pole[7] == pole[8] == player) \
        or (pole[0] == pole[3] == pole[6] == player)  or (pole[1] == pole[4] == pole[7] == player) or (pole[2] == pole[5] == pole[8] == player) \
        or (pole[0] == pole[4] == pole[8] == player) or (pole[2] == pole[4] == pole[6] == player):
        for i in btn:
            i.config(bg="lightgray", state="disabled")
        mb.showinfo("Игра окончена", "Победитель " + player + " ))")

def btn_disabled(num, t):
    if len(btn_num_clicked) > 0:
        pole[num] = t
        btn[num].config(text=t, state="disabled")
        btn_num_clicked.remove(num)

def btn_click(btn_num):
    global step   
    window.title(btn_num)
    btn_disabled(btn_num, "X")
    is_win("X")
    if btn_num == 4 and step == 0:
        btn_num_pl2 = rnd.choice(btn_num_clicked)
    elif btn_num != 4 and step == 0:        
        btn_num_pl2 = 4
    if step > 0:
        btn_num_pl2 = 8 - btn_num
        if btn_num_pl2 not in btn_num_clicked:
            btn_num_pl2 = rnd.choice(btn_num_clicked)
    btn_disabled(btn_num_pl2, "O")
    is_win("O")
    step += 1
        
btn = [tk.Button(font=28, height=3, width=6, command = lambda num=i: btn_click(num)) for i in range(9)]

row = 1
col = 0
for i in range(len(btn)):
    btn[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

window.mainloop()
```

## Задача 5.3
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

[Ссылка на dz5_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz5_3/dz5_3.py)
[Ссылка на input.txt](https://github.com/Leon2kk/GB_Python/blob/master/dz5_3/input.txt)
[Ссылка на output.txt](https://github.com/Leon2kk/GB_Python/blob/master/dz5_3/output.txt)

```sh
def encode(text):
	text_enc = ""
	i = 0
	while i < len(text):		
		cnt = 1
		while i + 1 < len(text) and text[i] == text[i + 1]:
			cnt += 1
			i += 1		
		text_enc += str(cnt) + text[i]
		i = i + 1
	return text_enc

def dencode(text:str):
    cnt = ""
    text_dec = ""
    for c in text:
        if c.isdigit():
            cnt += c
        else:
            text_dec += c * int(cnt)
            cnt = ''
    return text_dec

text_source = ''

# or input
with open('dz5_3\input.txt', 'r') as data:
    text_source = data.read()
data.close()

text_encode = encode(text_source)

#output
with  open('dz5_3\output.txt', 'w') as data:
    data.write(text_encode)
data.close()

text_dencode = dencode(text_encode)

print(text_source)
print(text_encode)
print(text_dencode)
```

# Семинар 4

## Задача 4.1
Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

[Ссылка на dz4_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz4_1.py)

```sh
n = int(input("Количество знаков в Pi = "))

Pi = 0 
for i in range(n):
    Pi +=  1 / (16 ** i) * ( 4 / (8*i + 1) -  2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6))

print(f"{Pi:.{n}f}")
```
## Задача 4.2
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

[Ссылка на dz4_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz4_2.py)

```sh
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
```
## Задача 4.3
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

[Ссылка на dz4_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz4_3.py)

```sh
list1 = [12, 34, 34, 12, 55, 6, 4, 5, 77, 56, 34, 9, 231, 43]
list2 = []

# list2 = set(list1)
# or
for i in list1:
    if i not in list2:
        list2.append(i)

print(list1, " -> ", list2)
```

## Задача 4.4
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

[Ссылка на dz4_4.py](https://github.com/Leon2kk/GB_Python/blob/master/dz4_4.py)

```sh
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
```

# Семинар 3

## Задача 3.1
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

[Ссылка на dz3_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_1.py)

```sh
n = [2, 3, 5, 9, 3]
s = 0

for i in range(len(n)-1):
    if i % 2 != 0:
        s += n[i]

print(s)
```

## Задача 3.2
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

[Ссылка на dz3_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_2.py)

```sh
n = [2, 3, 4, 5, 6]

n_len = len(n)

if n_len % 2 == 0:
    n_len = n_len // 2
else:
    n_len = n_len // 2 + 1

for i in range(n_len):
    print(n[i] * n[len(n) - i - 1])
```

## Задача 3.3
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

[Ссылка на dz3_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_3.py)

```sh
n = [1.1, 1.2, 3.1, 5, 10.01] #=> 0.19
m = list()

for i in range(len(n)):
    j = float("0." + str(n[i] * 1.0).split(".")[1])
    if j != 0:
        m.append(j)

print(max(m) - min(m))
```
## Задача 3.5
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

[Ссылка на dz3_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_5.py)

```sh
list_fibo = list()
a0 = 0
a1 = 1
n = int(input())

for i in range(n + 1):
    list_fibo.append(a0)
    x = a0 + a1
    a0 = a1
    a1 = x

list_fibo2 = [list_fibo[i] * (-1) ** (i + 1) for i in range(len(list_fibo))][::-1]

print(list_fibo2 + list_fibo[1:])
```
## Задача 3.6
Сдвиг списка.

[Ссылка на dz3_6.py](https://github.com/Leon2kk/GB_Python/blob/master/dz3_6.py)

```sh
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
```

# Семинар 2

## Задача 2.1
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

[Ссылка на dz2_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_1.py)

```sh
n = int(input("Введите N (количество монеток): "))

reshka = 0
for i in range(n):
    drop = random.randint(0, 1)
    print(drop)
    if (drop):
        reshka +=1

print("---\n", min(reshka, n-reshka))
```

## Задача 2.2
Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

[Ссылка на dz2_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_2.py)

```sh
n = int(input("Введите N: "))
print(int(((1 + n) / 2) * n))
```

## Задача 2.3
Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

[Ссылка на dz2_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_3.py)

```sh
n = int(input("Введите N: "))

flag = True
i = 2

while flag:
    if n % i == 0:
        print(i)   
        flag = False
    i += 1
```

## Задача 2.4
Петя впервые пришел на урок физкультуры в новой школе.Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

[Ссылка на dz2_4.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_4.py)

```sh
n = int(input("Введите N: (кол-во учеников): "))

list_rost = list()

for i in range(n):
    list_rost.append(int(input(f"рост {i + 1} ученика: ")))

rost = int(input("Ваш рост: "))

list_rost.sort(reverse = True)

j = 1
for i in list_rost:
    print(i)
    if rost <= i:
        j += 1

print("---\n", j)
```
## Задача 2.5
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

[Ссылка на dz2_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz2_5.py)

```sh
n = int(input("Введите N: "))

arr = list()

for i in range(n):
    arr.append(int(input()))

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i-1] + arr[i] + arr[i+1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

print(max(arr_count))
```


# Семинар 1

## Задача 1.1
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

[Ссылка на dz1_1.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_1.py)

```sh
d = int(input("Введите день недели: "))

if d >= 1 and d <= 5:
    print("Рабочий день")
elif d == 6 or d == 7:
    print("Выходной день")
else: 
     print("День недели указывается от 1 до 7")
```

## Задача 1.2
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

[Ссылка на dz1_2.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_2.py)

```sh
print("X | Y | Z |  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z | (1) = (2) |   = ")
print("-------------------------------------------------------------")

for x in range(2):
    for y in range(2):
        for z in range(2):
            v1 = int(not (x or y or z))
            v2 = int(not x and not y and not z)
            print(f"{x} | {y} | {z} |  ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} |   {v1} = {v2}   |  {v1 == v2}")

print("-------------------------------------------------------------")
```

## Задача 1.3
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


[Ссылка на dz1_3.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_3.py)

```sh
x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))

rez = " четверти"
if x > 0 and y > 0:
    rez = "в" + str(1) + rez
elif  x < 0 and y > 0:
    rez = "в" + str(2) + rez
elif  x < 0 and y < 0:
    rez = "в" + str(3) + rez
elif  x > 0 and y < 0:
    rez = "в" + str(4) + rez
elif  x == 0 and y == 0:
    rez = "в нач6але координат"
else:
    rez = ("на плоскости")

print(f"точка находится {rez}")
```

## Задача 1.4
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


[Ссылка на dz1_4.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_4.py)

```sh
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
```

## Задача 1.5
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


[Ссылка на dz1_5.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_5.py)

```sh
Ax, Ay = map(int, input("Введите координаты точки A(x, y), через пробел: ").split())
Bx, By = map(int, input("Введите координаты точки A(x, y), через пробел: ").split())

print("Расстояние между точками {:.2f}".format(((Bx - Ax) ** 2 + (By - Ay) ** 2) ** (0.5)))

```

## Задача 1.6
Числа Фибоначчи

[Ссылка на dz1_6.py](https://github.com/Leon2kk/GB_Python/blob/master/dz1_6.py)

```sh
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
```