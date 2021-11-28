#Написать скрипт, который выводит статистику для заданной папки в виде словаря,
#в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
#а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
#но больше предыдущей (начинаем с 0), например:
#{
#      100: 15,
#     1000: 3,
#      10000: 7,
#      100000: 2
#    }


import os

files_size_list = []
#os.chdir('../')

for dirpath, dirname, filenames in os.walk('./'):
    for file in filenames:
        path = os.path.join(dirpath, file)
        files_size_list.append((len(str(os.stat(path).st_size))))

list_size = set(files_size_list)
new_dict = {}
for i in list_size:
    new_dict[10**i] = files_size_list.count(i)
print(new_dict)






