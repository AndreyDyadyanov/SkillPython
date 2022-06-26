def name_surname(info):
    if info in data:
        return data[info]
    else:
        return ('Неизвестно', 'Неизвестно')

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

number = int(input('Введите номер паспорта: '))
series = int(input('Введите серию паспорта: '))

info = (number, series)

name, surname = name_surname(info)

print(f'Имя: {name}, Фамилия: {surname}')