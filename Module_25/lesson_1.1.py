class Dot:
    count = {'count': 0}

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.count['count'] += 1

    def __str__(self):
        return 'X = {}\nY = {}\nКоличество точек: {}'.format(self.__x, self.__y, self.count['count'])

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, coordinate):
        if isinstance(coordinate, int):
            self.__x = coordinate
        else:
            raise OSError('Неверный формат данных')

    def set_y(self, coordinate):
        if isinstance(coordinate, int):
            self.__y = coordinate
        else:
            raise OSError('Неверный формат данных')


coordinate_1 = Dot(1, 5)
coordinate_1.set_y(56)
coordinate_1.set_x(5)
coordinate_2 = Dot(1, 5)

print(coordinate_1)
print(coordinate_2)