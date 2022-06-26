office = int(input('Кол-во сотрудников в офисе: '))
office_list = []

for _ in range(office):

    employee_ID = int(input('ID сотрудника: '))

    office_list.append(employee_ID)

search_ID = int(input('Какого сотрудника ищем? '))
office_count = 0

for id in office_list:
    if search_ID == id:
        print('\nСотрудник на месте')
        break
    else:
        office_count += 1
        if office_count == office:
            print('\nСотрудник не работает!')

