#Есть два списка:tutors,klasses
#Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
#Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
# (<tutor>, None)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def klass_tutors(tut, klass):
    diff = len(klass) - len(tut)
    if diff > 0:
        for i in range(diff):
            tut.append('None')
    elif diff < 0:
        for i in range(diff):
            klass.append('None')
    for pair in range(len(tut)):
        yield (tut[pair], klass[pair])

print(*klass_tutors(tutors, klasses))

#Доказать, что вы создали именно генератор.
print(klass_tutors(tutors, klasses))
#Проверить его работу вплоть до истощения.
pair = klass_tutors(tutors, klasses)
print(type(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
print(next(pair))
#print(next(pair)) - истощение, ошибка




# Подумать, в каких ситуациях генератор даст эффект