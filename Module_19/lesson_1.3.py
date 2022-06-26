print('Текущие контакты на телефоне: \n<Пусто>')

phonebook = dict()

while True:
    name = input('Введите имя: ')

    if name in phonebook:
        print('Ошибка: такое имя уже существует.\n')
    else:
        number_phone = input('Введите номер телефона: ')
        phonebook[name] = number_phone

        print('\nТекущие контакты на телефоне:')

        for contact in phonebook:
            print('{0} {1}'.format(contact, phonebook[contact]))
        print()