import model, view

import os
os.system('cls') # чистим консоль

print('ТЕЛЕФОННЫЙ СПРАВОЧНИК')
var = input('1. Посмотреть записи\n2. Добавить запись\n3. Экспортировать в файл\n0. Выход\n-> ')

if var == '1':
    data = model.readAll()
    view.showToScreen(data)
if var == '2':
    fio = input("Введите ФИО: ")
    number = input("Введите телефон: ")
    model.add(fio, number)
    print("Сохранено!")
if var == '3':
    subvar = input(' 1. В формате TXT\n 2. В формате HTML\n 3. В формате XML\n 0. Выход\n-> ')    
    if subvar == '1':
        data = model.readAll()    
        view.saveToTXT(data)
        print("Сохранено!")  
    if subvar == '2':
        data = model.readAll()
        view.saveToHTML(data)
        print("Сохранено!")
    if subvar == '3':
        data = model.readAll()
        view.saveToXML(data)
        print("Сохранено!")