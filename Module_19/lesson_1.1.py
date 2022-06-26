number = int(input('Введите целое число: '))

number_list = [i_num for i_num in range(1, number + 1)]
number_dict = dict()
for i_num in number_list:
    number_dict[i_num] = int(i_num) ** 2

print(f'Результат: {number_dict}')