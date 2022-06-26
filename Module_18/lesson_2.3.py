text = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
name_list = input('Список людей через запятую: ').split(', ')
age_list = input('Возраст людей через пробел: ').split()

print()

for i in range(len(name_list)):
    print(text.format(name=name_list[i], age=age_list[i]))

people = [' '.join([name_list[i], age_list[i]]) for i in range(len(name_list))]

people_str = ', '.join(people)

print('\nСписок именинников: ', people_str)