import random

nums_1 = [random.randint(1, 30) for _ in range(30)]
nums_2 = [random.randint(1, 30) for _ in range(30)]

numbers_1 = set(nums_1)
numbers_2 = set(nums_2)

print('1-е множство: {}'.format(numbers_1))
print('2-е множство: {}'.format(numbers_2))

print('\nМинимальный элемент 1-го множества: {}'.format(numbers_1.pop()))
print('Минимальный элемент 2-го множества: {}'.format(numbers_2.pop()))

number_random_1 = random.randint(100, 200)
numbers_1.add(number_random_1)
print('\nСлучайное число для 1-го множества: {}'.format(number_random_1))

number_random_2 = random.randint(100, 200)
numbers_2.add(number_random_2)
print('Случайное число для 2-го множества: {}'.format(number_random_2))


result_1 = numbers_1 | numbers_2
print('\nОбъединение множеств: {}'.format(result_1))

result_2 = numbers_1 & numbers_2
print('Пересечение множеств: {}'.format(result_2))

result_3 = numbers_2 - numbers_1
print('Элементы входящие в nums_2, но не входящие в nums_1: {}'.format(result_3))
