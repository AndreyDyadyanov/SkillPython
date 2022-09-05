class Robot:

    def __init__(self, model):
        self.model = model

    def operate(self):
        pass


class Robot_vacuum_cleaner(Robot):

    def __init__(self, model):
        super().__init__(model)
        self.bag = 0

    def operate(self):
        if self.bag < 100:
            self.bag += 20
            print('Пылесошу пол. Мешок заполнен на {}%'.format(self.bag))
        else:
            print('Мешок заполнен на {}%'.format(self.bag))


class Robot_military(Robot):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('Защищаю военный объект с помощью оружия: {}'.format(self.gun))


class Submarine(Robot_military):
    def __init__(self, model, gun):
        super().__init__(model, gun)
        self.depth = 120

    def operate(self):
        print('Защищаю военный объект с помощью оружия: {} на глубине {} метров'.format(self.gun, self.depth))


robot_vacuum_cleaner = Robot_vacuum_cleaner('rvc-896')
robot_military = Robot_military('RM - 15', 'Пулемёт')
submarine = Submarine('Sub - 78', 'Торпеды')
robot_vacuum_cleaner.operate()
robot_military.operate()
submarine.operate()