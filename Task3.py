# Задайте список из n чисел последовательности (1+1/n)^n   
# и выведите на экран их сумму.

# Старый вариант
# list = []
# n = int(input('Введите число:'))
# sumnum = 0
# for i in range(1, n + 1):
#     sumnum = ((1+1/i)** i)
#     list.append(sumnum)    
# print(list)
# res = map(float, list)
# print(f'Сумма чисел: {sum(res)}')    

# Новый вариант

list = []
n = int(input('Введите число:'))
sumnum = [((1+1/i)** i) for i in range (1, n + 1)]  
print(sumnum)
print(f'Сумма чисел: {sum(sumnum)}')
    


