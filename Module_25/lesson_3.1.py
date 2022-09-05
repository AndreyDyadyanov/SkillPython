class Unit:
    def __init__(self):
        self.__hiptoins = 100

    def damage(self, damage=0):
        if self.__hiptoins > 0:
            __health = self.__hiptoins - damage
            print('Получено урона: {}, осталось здоровья: {}'.format(damage, __health))
        else:
            print('Погиб')

    def get_hiptoins(self):
        return self.__hiptoins

    def set_hiptoins(self, damage):
        self.__hiptoins -= damage


class Soldier(Unit):
    pass


class Citizen(Unit):

    def damage(self, damage=0):
        if self.get_hiptoins() > 0:
            self.set_hiptoins(damage * 2)
            print('Получено урона: {}, осталось здоровья: {}'.format(damage * 2, self.get_hiptoins()))
        else:
            print('Погиб')


solider = Soldier()
citizen = Citizen()
solider.damage(damage=20)
citizen.damage(damage=20)
solider.damage(damage=20)
citizen.damage(damage=20)
solider.damage(damage=20)
citizen.damage(damage=20)
solider.damage(damage=20)
citizen.damage(damage=20)


