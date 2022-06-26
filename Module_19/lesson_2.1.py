small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 100,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

product = input('Введите наименование товара: ')

if product in big_storage:
    print('Остаток на складе: {}'.format(big_storage.get(product)))
else:
    print('Ошибка, такого товара нет на складе!')

