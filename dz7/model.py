from datetime import datetime

def add(fio, number):
    with open('dz7/data.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{fio} | {number} | {datetime.now()}\n')

def readAll(showfile = 'dz7/data.txt'):
    with open(showfile, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        file.close()
        return lines 

        