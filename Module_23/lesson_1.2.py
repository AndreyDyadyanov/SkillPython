import random

name_list = list('AMKFLDKDHAKFKFJAHFALFKALF')

try:
    file_ages = open('ages.txt', 'r')
    file_result = open('result.txt', 'w', encoding='utf-8')
    file_result.write('Имя - Возраст\n')
    for age in file_ages:
        file_result.write('{} - {}'.format(random.choice(name_list), age))
    file_ages.close()
    file_result.close()
except FileExistsError:
    print('Попытка создания файла, котрый уже существует.')
except IsADirectoryError:
    print('На чтение ожидался файл, но это оказалась директория.')
except (TypeError, ValueError):
    print('Неверный тип данных или некорректное значение.')