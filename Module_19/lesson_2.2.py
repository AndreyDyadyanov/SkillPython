def min_income(dict):
    for i_income in dict.keys():
        if dict[i_income] == min(dict.values()):

            return i_income


incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00
}

print('Общий доход за год составил {} рублей'.format(sum(incomes.values())))
print('Самый маленький доход у {0}. Он составил {1} рублей'.format(min_income(incomes), min(incomes.values())))

incomes.pop(min_income(incomes))

print('Итогвый словарь: {}', format(incomes))