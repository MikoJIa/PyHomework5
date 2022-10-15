"""
Задание 4.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

numbers = int(input('Enter a positive integer number -  '))
#lst = [int(x) for x in str(numbers)] # Через список без индексов не получается найти!!!
Maximum = -1
#length = len(numbers)
while type(numbers) != int:
    try:
        numbers = int(numbers)
    except ValueError:
        print('Enter a positive integer number -  ')            

while numbers > 10: 
    num = numbers % 10
    numbers //= 10        
    if num > Maximum:
        Maximum = num
print(f'The largest digit in the number: {Maximum}')
# Если честно, эта задача далась сложно!! 