class CanFly:
    def __init__(self):
        self.__height = 0
        self.__speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def to_land(self):
        self.__height = 0
        self.__speed = 0
        print('Приземлились!\nВысота {}\tСкорость {}'.format(self.__height, self.__speed))

    def __str__(self):
        return 'Высота: {}\tСкорость: {}'.format(self.__height, self.__speed)

    def get_height(self):
        return self.__height

    def get_speed(self):
        return self.__speed

    def set_height(self, height):
        self.__height = height

    def set_speed(self, speed):
        self.__speed = speed


class Butterfly(CanFly):

    def take_off(self):
        self.set_height(1)
        print('Взлетели!\tВысота: {}'.format(self.get_height()))

    def fly(self):
        self.set_speed(0.5)
        print('Летим!\tСкорость: {}'.format(self.get_speed()))


class Rocket(CanFly):

    def take_off(self):
        self.set_height(500)
        self.set_speed(1000)
        print('Взлетели!\tВысота: {}\tСкорость: {}'.format(self.get_height(), self.get_speed()))

    def to_land(self):
        self.set_height(0)
        self.set_speed(0)
        print('Приземлились!\tВысота: {}\tВзрыв!'.format(self.get_height()))

    def explode(self):
        print('Ракета взорвалась на высоте {} при скорости {}'.format(self.get_height(), self.get_speed()))
        self.set_height(None)
        self.set_speed(None)


butterfly = Butterfly()
rocket = Rocket()
rocket.take_off()
rocket.explode()
print(rocket)

