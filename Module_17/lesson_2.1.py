a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

even_num = [x for x in range(a, b) if x % 2 == 0]

print(even_num)