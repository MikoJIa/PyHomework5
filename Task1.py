# Задание 1.
# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.
# Пример:
# Ведите ваше имя: Василий
# Ведите ваш пароль: vas
# Введите ваш возраст: 45
# Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
# """
Name = input('Enter your name: - ')
Password = input('Enter your password: - ')
Age = int(input('Enter your age: - '))
if Name == 'Nikolay' or Age == 45 or Password == 'vas':
    print('!!Welcome Nikolay!!')
    print(f'Your account login details: name - {Name}, password - {Password}, age - {Age}')
else:
    print('!!Access denied!!')    