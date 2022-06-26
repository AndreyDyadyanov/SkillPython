student_information = input('Введите информацию о студенте через пробел \n'
                            '(имя, фамилия, город, место учебы, оценки): ').split()

student_card = dict()

student_card['Имя'] = student_information[0]
student_card['Фамилия'] = student_information[1]
student_card['Город'] = student_information[2]
student_card['Место учебы'] = student_information[3]
student_card['Оценки'] = []

for i_grade in student_information[4:]:
    student_card['Оценки'].append(int(i_grade))


for i_info in student_card:
    print(f'\n{i_info} - {student_card[i_info]}')