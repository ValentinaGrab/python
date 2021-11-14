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

if __name__ == "__main__":
    get_valute = input('Введите код валюты: ')
    print(currency_rates(get_valute))

