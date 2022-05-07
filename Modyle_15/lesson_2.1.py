nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))

    nums_list.append(num)


for i in nums_list:

    if nums_list[0] <= i:
        maximum = i

    if nums_list[0] >= i:
        minimum = i

print('Максимальное число в списке:', maximum)

print('Минимальное число в списке:', minimum)