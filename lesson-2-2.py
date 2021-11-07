#Дан список:
#['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
#добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух
#целочисленных разрядов:
#['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(weather_list):
    if weather_list[i].isdigit() == True or weather_list[i] == '+5':
        if weather_list[i].isdigit() == True and int(weather_list[i]) < 10:
            weather_list[i] = '0' + weather_list[i]
        weather_list.insert(i+1,'"')
        weather_list.insert(i, '"')
        i += 2
        print(weather_list)
    i += 1
print(weather_list)
full_weather_message = ' '.join(weather_list)
weather_message = full_weather_message.split('"')
print(weather_message)
full_weather_message = '"'.join(weather_message)


print(full_weather_message)
#weather_message = full_weather_message.replace(' " ', ' "')

#print(weather_message)


#Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?