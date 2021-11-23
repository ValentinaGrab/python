#Для чтения данных реализовать в командной строке следующую логику:
#просто запуск скрипта — выводить все записи;
#запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
#запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
#Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
#Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.

import sys
from itertools import islice

error = 0
arg_exist = len(sys.argv[1:])
for item in sys.argv[1:]:
    if item.isdigit() == False:
        error += 1
if error == 0:
    if arg_exist == 1:
        arguments = sys.argv[1:]
        with open('bakery.csv', 'r', encoding='utf-8') as file_1:
            print(*islice(file_1, int(arguments[0])-1, None))
    elif arg_exist == 0:
        with open('bakery.csv', 'r', encoding='utf-8') as file_1:
            for line in file_1:
               print(line.rstrip())
    elif arg_exist == 2:
        arguments = sys.argv[1:]
        with open('bakery.csv', 'r', encoding='utf-8') as file_1:
            print(*islice(file_1, int(arguments[0])-1, int(arguments[1])))
    else:
        print('Слишком много аргументов')
else:
    print('Такие аргументы вводить нельзя')


