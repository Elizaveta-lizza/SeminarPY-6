# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
try:
    number = int(input('Введите длину массива: '))
    min_number = int(input('Введите минимальное число: '))
    max_number = int(input('Введите максимальное число: '))
    array = []
    for i in range(number+1):
        i = random.randint(1,10)
        array.append(i)
    print(array)
    for i in range(len(array)):
        if min_number <= array[i] <= max_number:
            print(f'Число которое входят в диапозон равно {array[i]}. Индекс числа равен {i}')
except:
  print('Введены некорректные данные')
        
        
