import os
import random

def search_path(path, file):
    for elem in os.listdir(path):
        res_path = os.path.join(path, elem)

        if file == elem:
            print(res_path)
            path_list.append(res_path)

        if os.path.isdir(res_path):
            search_path(res_path, file)




path = input('Ищем в: ')
name_file = input('Имя файла: ')
path_list = []

print('Найдены следующие пути: ')

search_path(path, name_file)

print()

number = random.randint(0, len(path_list))

file = open(path_list[number], 'r', encoding='utf-8')
data = file.read()
print(data)
file.close()