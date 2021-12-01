#Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

import requests

def currency_rates(item):
 item = item.upper()
 print(item)
 data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
 if item in data['Valute']:
  curs = data['Valute'][item]['Value']
#  print(type(curs)) # float
  date_curs = data['Date']
#  print(type(date_curs)) #str
  return f"{curs} Date {date_curs[:10]}"
 else:
  return None

get_valute = input('Введите код валюты: ')
print(currency_rates(get_valute))

