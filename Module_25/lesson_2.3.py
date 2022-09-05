class DivisionError(Exception):
    pass


with open('numbers.txt', 'r') as file:
    for numbers in file:
        try:
            pair = numbers.split()
            denominator = int(pair[0])
            divider = int(pair[1])
            if denominator < divider:
                raise DivisionError('Нельзя делить меньшее на большее')
            else:
                result = denominator / divider
                print(result)
        except DivisionError:
            print('Нельзя делить меньшее на большее')
