path = input('Путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
extension = input('Требуемое расширение файла: ')


if not path.endswith(extension):
    print('Неверное расширение файла!')
elif not path.startswith(disk):
    print('Неправильно указан диск!')
else:
    print('Путь корректен!')