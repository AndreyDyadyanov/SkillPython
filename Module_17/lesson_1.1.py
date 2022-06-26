left = int(input('Левая граница: '))
right = int(input('Правая граница: '))

first_list = [x ** 3 for x in range(left, right + 1)]
second_list = [x ** 2 for x in range(left, right + 1)]

print('\nСписок кубов чисел в диапазоне от', left, 'до', str(right) + ':', first_list)
print('Список квадратов чисел в диапазоне от', left, 'до', str(right) + ':', second_list)