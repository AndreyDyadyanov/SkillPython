import random

alphabet  ='абвгдеёжзиёклмнопрстуфхцчшщъыьэюя'

first = [random.choice(alphabet) for _ in range(10)]
second = [random.choice(alphabet) for _ in range(10)]

print('Первый список: {}'.format(first))
print('Второй список: {}'.format(second))

first_dict = {index: symbol for index, symbol in enumerate(first)}
second_dict = {index: symbol for index, symbol in enumerate(second)}

print('\nПервый словарь: {}'.format(first_dict))
print('Второй словарь: {}'.format(second_dict))