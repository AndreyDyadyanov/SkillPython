phone_book = dict()
print('Текущий список контактов: {}'.format(phone_book))
while True:
    for name, number in phone_book.items():
        print('Текущий список контактов: {firstName} {secondName} - {phone}'.format(
            firstName=name[0],
            secondName=name[1],
            phone=number
        )
        )

    name = input('\nВведите имя: ')
    surname = input('Введите фамилию: ')
    number_phone = int(input('Введите номер телефона: '))

    key = (name, surname)

    phone_book[key] = number_phone