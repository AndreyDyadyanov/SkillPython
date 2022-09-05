class Family():
    surmame = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            'Family name: {}\nFamily funds: {}\nHaving a house: {}'.format(
            self.surmame, self.money, self.have_a_house
            )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current value {}'.format(amount, self.money))

    def bye_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}\n'.format(self.money))
        else:
            print('Not enought money!\n')



family = Family()
family.info()

print('\nTry to buy house')
family.bye_house(1000000)

if not family.have_a_house:
    family.earn_money(800000)
    print('Try to buy a house again')
    family.bye_house(1000000, 10)

family.info()