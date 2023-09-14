from datetime import datetime
import os

def id(line):                                                                   # Извлечение id из строки
   mass = line.split(";")
   return int (mass[0])

def time_code():                                                                # Формирует id из времени для формирования списка поиска сообщений
    now=datetime.now()
    year = input("Введите полный год: ")
    if year == "": year=now.strftime("%Y")
    month = input("Введите месяц двухзначным числом: ")
    if month == "": month="01"
    day = input("Введите день двухзначным числом: ")
    if day == "": day="01"
    hour = input("Введите час двухзначным числом по 24h: ")
    if hour == "": hour="00"
    return int (year+month+day+hour+"0000")

def show():                                                                     # Печать всей базы
    with open(FILE_PATH,'r',encoding='utf-8') as base:
        print(base.read())

def add():                                                                      # Добавление новой записи в файл
    now=datetime.now()                                                          # текущее время
    new_id=now.strftime("%Y%m%d%H%M%S")                                         # формируется id из времени создания или редактирования
    date=now.strftime("%d.%m.%Y %H:%M")                                         # Формирование текущего времени для записи в строку
    name=input("Введите название заметки: ")
    notes=input("Напишите заметку: ")

    with open(FILE_PATH,'a',encoding='utf-8') as base:
        base.write(new_id+';'+date+';'+name+';'+notes+'\n')

def search():                                                                   # Формирование списка запроса заметок по времени
    print("[1] Вывести все сообщения ДО введенного времени")
    print("[2] Вывести все сообщения ПОСЛЕ введенного времени")
    print("[3] Вывести все сообщения в промежутке введенного времени")
    incom =int(input("Выберите режим поиска: "))
    if incom == 1:
        id_find = time_code()
        with open(FILE_PATH,'r',encoding='utf-8') as base:
            while True:
                info=base.readline()
                if info:
                    if id(info)<=id_find:
                        print(info)
                else:
                    break
    elif incom ==2:
        id_find = time_code()
        with open(FILE_PATH,'r',encoding='utf-8') as base:
            while True:
                info=base.readline()
                if info:
                    if id(info)>=id_find:
                        print(info)
                else:
                    break
    elif incom ==3:
        print("C какого времени искать")
        id_find_star = time_code()
        print("Каким временем закончить")
        id_find_end =time_code()
        with open(FILE_PATH,'r',encoding='utf-8') as base:
            while True:
                info=base.readline()
                if info:
                    if id_find_star<id(info) <=id_find_end:
                        print(info)
                else:
                    break

def edit():                                                                   # Изменение найденой записи
    index=int(input("Введите id строки для замены: "))
    with open(FILE_PATH,'r',encoding='utf-8') as base1:                       # Открытие файла на чтение текущей базы
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as base2:              # Открытие файла для записи новой базы
            while True:
                info=base1.readline()
                if info:
                    if index != id(info):                                     # Переписывает всю базу до тех пор пока не найдет запись для изменения
                        base2.write(info)
                    else:
                        print(info)                                           # Печатает найденую заметку (чтобы пользователь не ошибся в изменениях)
                        now=datetime.now()                                                          
                        new_id=now.strftime("%Y%m%d%H%M%S")                   # Формирует новый id                          
                        date=now.strftime("%d.%m.%Y %H:%M")                   # Формирует новое время изменения заметки                    
                        name=input("Введите новое название заметки: ")
                        notes=input("Напишите заметку: ")
                        no_whrite=input("Если хотите изменить заметку наберите [1], если нет наберите [0] ") # Запрашивает подтверждение на изменение заметки
                        if int (no_whrite) ==1:
                            base2.write(new_id+';'+date+';'+name+';'+notes+'\n') # Изменяет заметки
                        else:
                            base2.write(info)                                 # Переписывает остаток базы в новый временный файл
                else:
                    break
    os.remove(FILE_PATH)                                                      # Удаляет старую базу
    os.rename(FILE_PATH_TEMP,FILE_PATH)                                       # Переименовывает временную базу в текущию

def delete():                                                                   # Удаление выбранной строки
    index=int(input("Введите id строки: "))
    with open(FILE_PATH,'r',encoding='utf-8') as base1:
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as base2:
            while True:
                info=base1.readline()
                if info:
                    if index != id(info):
                        base2.write(info)
                else:
                    break
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TEMP,FILE_PATH)
    print("Все готово")


FILE_PATH = r"control_work_01\base.txt"                                             # Начальная база
FILE_PATH_TEMP = r"control_work_01\base_temp.txt"                                   # Временная база

while True:
    print()                                                                 # Печать списка допустимых команд
    print('[1] Показать весь список заметок')
    print('[2] Добавить')
    print('[3] Поиск')
    print('[4] Редактировать')
    print('[5] Удалить')
    print('[6] Выход')
    print()
    Command = int(input("Введите номер команды: "))

    if Command ==1:                                                                 # Выполнение команды
        show()
    elif Command==2:
        add()
    elif Command==3:
        search()
    elif Command==4:
        edit()
    elif Command==5:
        delete()
    else: break