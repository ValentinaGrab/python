#Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
#src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [23, 1, 3, 10, 4, 11]
#Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
import sys
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
def only_one_in_list(spisok):
    for item in spisok:
        if spisok.count(item) == 1:
            yield item

result = list(only_one_in_list(src))
print(result, 'Size:', sys.getsizeof(result), 'Time: ', perf_counter() - start)

#Потом подумайте об оптимизации.
start = perf_counter()
only_one_num = [item for item in src if src.count(item) == 1]
print(only_one_num, 'Size:', sys.getsizeof(only_one_num), 'Time: ', perf_counter() - start) #этот вариант работает быстрее
