# Семинар 5.
# Задание № 1.

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

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