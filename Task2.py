"""
Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_second = int(input('Enter time in second - '))
hour = (time_second/3600)
minuts = (time_second/60)
seconds = 3600 % (24 * 3600) 
print(f'Time in the format: h:m:s - {hour} : {minuts} : {seconds}') # Ф-строки
print('Time in the format: h:m:s - {} : {} : {}'.format(hour, minuts, seconds)) # Формат строк
