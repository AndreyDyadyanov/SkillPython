dogs = int(input('Введите кол-во собак: '))
coin_dog_list = []
new_coin_dog_list = []

for i in range(1, dogs + 1):
    print('Введите кол-во очков у', i, 'собаки:', end = ' ')
    coin_dog = int(input())
    coin_dog_list.append(coin_dog)

min = coin_dog_list[0]
max = coin_dog_list[0]

for i in range(dogs):
    if coin_dog_list[i] <= min:
        min = coin_dog_list[i]
    if coin_dog_list[i] >= max:
        max = coin_dog_list[i]

for coin in coin_dog_list:
    if coin == min:
        new_coin_dog_list.append(max)
    elif coin == max:
        new_coin_dog_list.append(min)
    else:
        new_coin_dog_list.append(coin)

print('Старый список:', coin_dog_list)
print('Новый список:', new_coin_dog_list)