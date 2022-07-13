import os

def search_path(path, file):
    for elem in os.listdir(path):
        res_path = os.path.join(path, elem)

        if file + '.py' == elem:
            print(res_path)

        if os.path.isdir(res_path):
            search_path(res_path, file)




path = input('Ищем в: ')
name_file = input('Имя файла: ')

print('Найдены следующие пути: ')

search_path(path, name_file)