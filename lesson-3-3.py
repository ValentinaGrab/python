def names_dict(names_list):
    dict = {}
    for i in range(len(names_list)):
        if dict.get(names_list[i][0]) != None:
            names = dict.get(name_list[i][0])
            dict[name_list[i][0]] = names + " " + names_list[i]
#           print('изменить элемент по ключу')
        else:
            dict.setdefault(name_list[i][0], name_list[i])
#           print(dict)
        i += 1
    return dict

name_list = []
for i in range(5):
    name_list.append(input('Input name:'))
print('Вы ввели имена: ', name_list)
print("Справочник имен:\n", names_dict(name_list))










