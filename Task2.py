# 1'. Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Старый вариант
# import random
# n = int(input('Введите число:'))
# some_list = [random.randint(-n, n) for i in range(n)]
# print(some_list, ' -> на нечётных позициях элементы: ', end='')
# sum = 0
# for i in range(1, n, 2):
#     sum += some_list[i]
#     print(some_list[i], end=', ')
# print('ответ: ', sum)

# Новый вариант

import random

n = int(input('Введите число:'))
some_list = [random.randint(-n, n) for i in range(n)]
print(some_list, ' -> на нечётных позициях элементы: ', end='')
some_list_2 = [some_list[i] for i in range(1,len(some_list),2)]
print(sum(some_list_2))