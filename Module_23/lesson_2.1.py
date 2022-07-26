file = open('user_data.txt', 'w')
try:
    user_text = input('Введите строку: ')
    file.write(user_text)
except (TypeError, ValueError):
    print('Нельзя преобразовать данные в целое число.')
except OSError:
    print('Проблема при открытии файла')
except:
    print('Неожиданная ошибка!')

else:
    print('Данные успешно записаны!')
finally:
    file.close()
    print('Файл закрыт: {}'.format(file.closed))
