emp_amount = int(input('Кол-во сотрудников: '))
income_list = []

for i in range(emp_amount):
    print('Зарплата', i + 1, 'сотрудника:', end=' ')
    income = int(input())
    income_list.append(income)
    if income == 0:
        income_list.remove(income)

print('\nОсталось сотрудников:', len(income_list))
print('\nЗарплаты:', income_list)

print('\nМаксимальная зп:', max(income_list))
print('Минимальная зп:', min(income_list))
