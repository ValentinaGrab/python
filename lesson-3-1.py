#Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например
#>>> num_translate("one")
#"один"
#>>> num_translate("eight")
#"восемь"

def num_translate(ru_num):
    dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'zero': 'ноль'
    }
    if ru_num in dictionary.keys():
        return dictionary[ru_num]
    else:
        return None

num = input("Введи число от 0 до 10 на английском языке:")
print('\nПеревод на русский', num_translate(num))

