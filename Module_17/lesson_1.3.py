def promotion(year, price):
    return round(price * (1 + year / 100), 2)

price_list = [float(input('Цена на товар: ')) for _ in range(5)]


second_promotion = []

first_year = int(input('Повышение на первый год: '))
second_year = int(input('Повышение на второй год: '))

first_promotion = [promotion(first_year, i) for i in price_list]
second_promotion = [promotion(second_year, i) for i in first_promotion]

print('Сумма за каждый го д:', round(sum(price_list), 2), round(sum(first_promotion), 2), round(sum(second_promotion), 2))