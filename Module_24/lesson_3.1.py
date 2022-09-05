class Toyota:
    color = 'красный'
    price = 1000000
    max_speed = 200
    speed_now = 0

    def __init__(self, color, price, max_speed, speed_now):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.speed_now = speed_now

    def info(self):
        print('Цвет: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}'.format(
            self.color, self.price, self.max_speed, self.speed_now)
        )

    def real_time_speed(self, speed):
        self.speed_now = 0
        self.speed_now += speed
        print('\nТекущая скорость: {}'.format(self.speed_now))

car_1 = Toyota('Зеленый', 1500000, 180, 100)
car_2 = Toyota('Синий', 2000000, 250, 20)

car_1.info()
car_2.info()

car_2.real_time_speed(50)
car_2.real_time_speed(30)