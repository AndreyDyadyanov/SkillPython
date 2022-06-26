goods = [
    ['яблоки', 50], ['апельсины', 190], ['груши', 100],
    ['нектарины', 200], ['бананы', 77]
]

print('Текущий ассортимент:', goods)

new_fruit = []

fruit_name = input('Новый фрукт: ')
new_fruit.append(fruit_name)

price = int(input('Цена: '))
new_fruit.append(price)

goods.append(new_fruit)

print('\nНовый ассортимент:', goods)

for i in range(len(goods)):
    goods[i][1] = round(goods[i][1] * 1.08, 2)

print('\nНовый ассортимент с увел.ценой:', goods)


