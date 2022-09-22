# Семинар 5.
# Задание № 1 a, b.

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

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