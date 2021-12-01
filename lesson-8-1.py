#Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
#>>> email_parse('someone@geekbrains.ru')
#{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  ...
#    raise ValueError(msg)
#ValueError: wrong email: someone@geekbrainsru
#Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

RE_EMAIL = re.compile(r'([a-zA-Z0-9._-]+)\@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})+$')

def mail_parse(name):
    m = RE_EMAIL.match(name)
    if m:
        return {'Username:': m.groups()[0], 'Domain':m.groups()[1]}
    else:
        return "Неверный формат e-mail"

print(mail_parse('kopallochka@ail.ru'))

