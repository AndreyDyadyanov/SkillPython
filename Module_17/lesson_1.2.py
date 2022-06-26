words = input('Введите строку: ')
symbols = input('Введите символ: ')

double = [x * 2 for x in words]
plus_symbol = [x + symbols for x in double]

print('\nСписок удвоенных символов:', double)
print('Склейка с дополнительным символом:', plus_symbol)