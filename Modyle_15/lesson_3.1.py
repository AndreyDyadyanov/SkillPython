text = input('Введите строку: ')

symbols = list(text)
symbols_count = 0
new_list = []

for i in symbols:
    if i == ':':
        i = ';'
        symbols_count += 1

    new_list.append(i)

print('\n\nИсправленная строка:', end=' ')

for i in new_list:
    print(i, end='')

print('\nКол-во замен:', symbols_count)