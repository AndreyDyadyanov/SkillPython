str_input = input('Введите строку: ')

counter = [0, 0]

for letter in str_input:
    if letter.islower():
        counter[0] += 1
    elif letter.isupper():
        counter[1] += 1

if counter[0] > counter[1]:
    print('Результат:', str_input.lower())
elif counter[1] > counter[0]:
    print('Результат:', str_input.upper())
else:
    print('Ничья')