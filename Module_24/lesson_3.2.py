class Dot:
    count = {'count': 0}

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.count['count'] += 1

    def info(self):
        print('X = {}\nY = {}'.format(self.x, self.y))
        print('Количество точек: {}'.format(self.count['count']))


coordinate_1 = Dot(5, 10)
coordinate_2 = Dot(9, 13)
coordinate_3 = Dot(18, 36)
coordinate_4 = Dot(21, 14)
coordinate_4.info()
