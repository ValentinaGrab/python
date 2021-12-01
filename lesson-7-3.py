#Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates
#
#|--my_project
#   |--settings
#   |  |--dev.py
#   |  |--prod.py
#   |--mainapp
#   |  |--__init__.py
#   |  |--models.py
#   |  |--views.py
#   |  |--templates
#   |     |--mainapp
#   |        |--base.html
#   |        |--index.html
#   |--authapp
#   |  |--models.py
#   |  |--views.py
#   |  |--templates
#   |     |--authapp
#   |        |--base.html
#   |        |--index.html

import os
import shutil

folders = {'settings': ['dev.py','wert.py'],
            'mainapp': ['__init__.py', 'models.py', 'views.py',  {'templates': {'mainapp': ['base.html', 'index.html']}}],
            'adminapp': ['models.py', 'views.py', {'templates' : {'authapp': ['base.html', 'index.html']}}]
           }
main_folder = 'my_project_'

#path = [os.makedirs(os.path.join(main_folder, i)) for i in folders if not os.path.exists(os.path.join(main_folder, i))]

def rec(main_folder, folders_dict):
    print('Вход', main_folder, folders_dict)
    path = [os.makedirs(os.path.join(main_folder, i)) for i in folders_dict if
            not os.path.exists(os.path.join(main_folder, i))]
    for key in folders_dict:
         print(key, folders_dict[key])
         if type(folders_dict[key]) == dict:
             new_dict = folders_dict[key]
             new_path = os.path.join(main_folder, key)
             rec(new_path, new_dict)
         else:
             for i in range(len(folders_dict[key])):
                print(folders_dict[key][i])
                if type(folders_dict[key][i]) == str:
                    file_path = os.path.join(main_folder, key, folders_dict[key][i])
                    with open(file_path, 'w', encoding='utf-8') as file_1:
                        print('Создать файл')
                elif type(folders_dict[key][i]) == dict:
                        print('создать папку')
                        new_dict = folders_dict[key][i]
                        print(os.path.join(main_folder, key))
                        rec(os.path.join(main_folder, key), new_dict)
rec(main_folder, folders)
files_to_copy = []
my_dir = 'Task_3'

for dirpath, dirname, filenames in os.walk(main_folder):
    for file in filenames:
        print(file)
        if '.html' in file:
#            print(file)
            files_to_copy.append(os.path.join(dirpath, file))
#            print(files_to_copy)
for path in files_to_copy:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.makedirs(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    print(save_path)
    shutil.copy(path, save_path)
