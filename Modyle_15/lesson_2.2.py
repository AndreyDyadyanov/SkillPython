nums = int(input('Кол-во чисел в списке: '))
num_list = []

for i in range(1, nums + 1):
    print('Введите', i, 'число:', end = ' ')
    number = int(input())
    num_list.append(number)

print()
divider = int(input('Введите делитель: '))
print()

index_summ = 0

for i in range(nums):
    if num_list[i] % divider == 0:
        index_summ += i
        print('Индекс числа', str(num_list[i]) + ':', i)

print('Сумма индексов:', index_summ)