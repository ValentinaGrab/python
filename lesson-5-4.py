#Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего,
# например:
#src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#result = [12, 44, 4, 10, 78, 123]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def condition_list(cur_list):
    for item in range(1, len(cur_list)):
        if cur_list[item] > cur_list[item-1]:
            yield cur_list[item]

result = list(condition_list(src))
print('Эти элементы списка больше предыдущих: ', result)
