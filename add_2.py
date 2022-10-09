#Чётные элементы по значению увеличить на 5, нечетные занулить

from random import randint

while True: 
    try:
        lenth = int(input("Введите длину массива целым числом: "))
        break
    except (TypeError, ValueError):
        print ('Это не целое число, пожалуйста, введите целое число')

a = [0] * lenth                 # массив
        
for i in range(lenth):
    a[i] = randint(-20, 20)     # Набор элементов из которых будет состоять массив
print("Входной массив: ")
print(a)

for i in range(lenth):    
    if a[i] % 2 == 0:
        a[i]+=5
    else: 
        a[i] = 0
print("Массив где все чётные числа увеличены на 5, а нечётные занулены: ")  
print(a)