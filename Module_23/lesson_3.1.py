symbols_count = 0
length = 0

try:
    file_name = open('name.txt', 'r')
    for name in file_name:
        length += 1
        lenght_name = len(name)
        if name.endswith('\n'):
            lenght_name -= 1
        if lenght_name < 3:
            raise BaseException('Длина строки {} меньше трёх символов'.format(length))
        symbols_count += lenght_name
except FileNotFoundError:
    print('Файл не найден')
finally:
    print('Общая сумма символов: {}'.format(symbols_count))

