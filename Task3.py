"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""
user_1 = int(input('Enter a positive integer n - '))
user_2 = user_1 * 2
user_3 = user_1 ** 2
print(f'{user_1}{user_2}{user_3}')