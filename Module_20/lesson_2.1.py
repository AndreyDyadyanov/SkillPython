line = input('Строка: ')

print('\nОтвет:', end=' ')
for index, symbol in enumerate(line):
    if symbol == '~':
        print(index, end=' ')