text = input('Введите строку: ')
number = int(input('Номер символа: '))

symbols = list(text)
symbol_count = 0

print('\nСимвол слева:', symbols[number - 2])
print('Символ справа:', symbols[number])

for i in symbols:
    if i == symbols[number - 1]:
        symbol_count += 1

if symbol_count == 1:
    print('\nТаких же символов нет.')
elif symbol_count == 2:
    print('\nЕсть ровно один такой же символ.')
elif symbol_count == 3:
    print('\nЕсть ровно два таких же символа.')
