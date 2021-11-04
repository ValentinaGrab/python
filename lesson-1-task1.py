#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration_format = [" сек", " мин ", " час ", " день "]
duration_length = [60, 60, 24, 365]
result_time = " "
duration_sec = int(input("Введите продолжительность в секундах: "))
print("\nСекунды: ", duration_sec)
#Если введенное значение меньше или равно 60, то нет смысла делить
if duration_sec <= 60:
    result_time = str(duration_sec) + duration_format[0]
#Если введенное значение больше 60, то делим значение на элементы списка duration_length
else:
    for i in range(len(duration_length)):
        result_time =  str(duration_sec % int(duration_length[i])) + str(duration_format[i]) + result_time
        duration_sec = duration_sec // duration_length[i]
        if duration_sec == 0:
            break
        i+=1

print("Длительность в формате: ", result_time)
