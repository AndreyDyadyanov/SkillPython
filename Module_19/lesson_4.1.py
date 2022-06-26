line = input('Введите строку: ')

symbols = {'.', ',', ';', ':', '!', '?'}

count = 0

for symbol in line:
    if symbol in symbols:
        count += 1

print('Количество знаков пунктуации: {}'.format(count))

# Я! Есть. Грут?! Я, Грут и Есть.