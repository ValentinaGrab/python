#Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield:
import sys

def odd_nums(max_nums):
    for num in range(1, max_nums + 1, 2):
        yield num

print(*odd_nums(15))

#** (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield
print(*(num for num in range(1, 16, 2)))

