num_list = []

for i in range(4):
    num = int(input('Введите число: '))

    if num < 0 or num > 255:
        print('Ошибка! Число должно находится в диапазоне от 0 до 255 (включительно).')
        break
    else:
        num_list.append(num)

if len(num_list) == 4:
    ip_address = '{0}.{1}.{2}.{3}'.format(
        num_list[0],
        num_list[1],
        num_list[2],
        num_list[3]
    )

    print(ip_address)