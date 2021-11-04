#Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
list_kub = []
list_sum_number = []
sum_number = 0
sum_total = 0

for i in range(1, 1001, 2):
    list_kub.append(i**3)
print(list_kub)

#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.


for i in range(len(list_kub)):
    number = int(list_kub[i])
#    print(number)
    sum_number = 0
    while number != 0:
        sum_number = sum_number + number % 10
        number = number // 10
    if sum_number % 7 == 0:
        list_sum_number.append(list_kub[i])
        sum_total = sum_total + int(list_kub[i])

print("\n Список из элементов, сумма цифр которых кратна 7: ", list_sum_number)
print("\n Сумма элементов, сумма цифр которых кратна 7: ", sum_total)

#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.

for i in range(len(list_kub)):
    list_kub[i] = int(list_kub[i])+17
print("Список после прибавления 17: ", list_kub)
sum_total = 0
list_sum_number.clear()

for i in range(len(list_kub)):
    number = int(list_kub[i])
#    print(number)
    sum_number = 0
    while number != 0:
        sum_number = sum_number + number % 10
        number = number // 10
    if sum_number % 7 == 0:
        list_sum_number.append(list_kub[i])
        sum_total = sum_total + int(list_kub[i])

print("\n Список из элементов, сумма цифр которых кратна 7: ", list_sum_number)
print("\n Сумма элементов, сумма цифр которых кратна 7: ", sum_total)
