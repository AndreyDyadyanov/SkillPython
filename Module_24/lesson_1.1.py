import random

class Toyota:
    color = 'красный'
    price = 1000000
    max_speed = 200
    speed_now = 0

car_1 = Toyota()
car_1.speed_now = random.randint(0, 200)
car_2 = Toyota()
car_2.speed_now = random.randint(0, 200)
car_3 = Toyota()
car_3.speed_now = random.randint(0, 200)

print(car_1.speed_now, car_2.speed_now, car_3.speed_now)