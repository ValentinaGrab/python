import sys

def isfloat_(str):
    try:
        float(str)
    except:
        return False

arg_exist = len(sys.argv[1:])
if arg_exist == 0:
    print('Укажите сумму проданной булочки')
else:
    if arg_exist > 1 or isfloat_(sys.argv[1]) == False:
        print('Недопустимые аргументы')
    else:
        with open('bakery.csv', 'a', encoding='utf-8') as file_1:
            file_1.writelines('\n'+sys.argv[1])
            print('Данные успешно записаны')
