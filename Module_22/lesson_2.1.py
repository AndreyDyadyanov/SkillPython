import os

path = os.path.abspath(os.path.join('..', 'Module_17', 'lesson_1.2.py'))

print('Путь', path)

if os.path.exists(path):
    if os.path.isdir(path):
        print('Это директория')
        print('Размер файла:', os.path.getsize(path), 'байт')

    elif os.path.isfile(path):
        print('Это файл')
        print('Размер файла:', os.path.getsize(path), 'байт')

    elif os.path.islink(path):
        print('Это ссылка')
        print('Размер файла:', os.path.getsize(path), 'байт')

else:
    print('Указанного пути не существует')