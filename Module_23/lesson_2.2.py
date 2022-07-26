import random

name_list = list('AMKFLDKDHAKFKFJAHFALFKALF')
file_ages = open('ages.txt', 'r')
file_result = open('result.txt', 'w', encoding='utf-8')
try:
    file_result.write('Имя - Возраст\n')
    for age in file_ages:
        if int(age):
            file_result.write('  {} - {}'.format(random.choice(name_list), age))
except FileExistsError:
    print('Попытка создания файла, котрый уже существует.')
except IsADirectoryError:
    print('На чтение ожидался файл, но это оказалась директория.')
except (TypeError, ValueError):
    print('Неверный тип данных или некорректное значение.')
else:
    print('Прорамма выполнена успешно!')
finally:
    file_ages.close()
    file_result.close()
    print('Файл ages закрыт: {}\nФайл reslt закрыт: {}'.format(file_ages.closed, file_result.closed))