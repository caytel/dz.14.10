# 1. Найти количество элементов в заданном массиве ARRAY,
# отличающихся от минимального на DELTA
# Комментарий: array = [1,2,3,5] delta = 4 Вывод: 1

from random import randint

print("Вводите, пожалуйста, только целые числа")

while True:
    try: 
        delta = int(input("Введите дельта: "))
        lenth = int(input("Введите длину массива: "))
        break
    except (TypeError, ValueError):
        print ('Это не целое число, пожалуйста, введите целое число')
        
min_el = 10 * 6
k = 0                           # Количество элементов
a = [0] * lenth                 # массив

for i in range(lenth):
    a[i] = randint(-15, 15)     # Набор элементов из которых будет состоять массив
print("Первоначальный массив: ")
print(a)

for i in range(lenth):          # Поиск минимального
    if a[i] < min_el:
        min_el = a[i]

for i in range(lenth):          # Проверка условия задачи
    if (min_el + delta) == a[i]:
        k += 1
        
print("Количество элементов, отличающихся от минимума на", delta, " = ", k)