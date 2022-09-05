class Toyota:
    color = 'красный'
    price = 1000000
    max_speed = 200
    speed_now = 0

    def info(self):
        print('Цвет: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}'.format(
            self.color, self.price, self.max_speed, self.speed_now)
        )

    def real_time_speed(self, speed):
        self.speed_now = 0
        self.speed_now += speed
        print('\nТекущая скорость: {}'.format(self.speed_now))


car_1 = Toyota()
car_1.info()
car_1.real_time_speed(100)
car_1.real_time_speed(100)
