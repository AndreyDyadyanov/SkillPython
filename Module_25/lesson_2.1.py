class Ship:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return 'Модель корабля {}'.format(self.model)

    def sail(self):
        print('\nКорабль в пути')


class WarShip(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('Корабль атакует с помощью оружия: {}'.format(self.gun))


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def loading(self):
        if self.tonnage_load < 100:
            print('\nИдет погрузка корабля...')
            self.tonnage_load += 100
            print('Корабль загружен на {} процентов'.format(self.tonnage_load))
        else:
            print('\nПогрузка не может быть осуществлена. Корабль уже загружен!')

    def unloading(self):
        if self.tonnage_load > 0:
            print('\nИдет разгрузка корабля...')
            self.tonnage_load -= 100
            print('Разгрузка завершена!')
            print('Корабль загружен на {} процентов'.format(self.tonnage_load))
        else:
            print('\nРазгружать нечего. Корабль пустой!')


war_ship = WarShip('ED89', 'Пушка')
cargo_ship = CargoShip('OPSIS')
print(war_ship)
print(cargo_ship)
war_ship.attack()
cargo_ship.loading()
cargo_ship.unloading()
