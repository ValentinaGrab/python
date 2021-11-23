#Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

from utils import currency_rates

currencys = ('GBP', 'USD', 'EUR', 'CNY', 'UAH')

for item in currencys:
    print(currency_rates(item))

