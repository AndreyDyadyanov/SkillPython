family_member = dict()

family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ['running', 'sky diving', 'singing']
family_member['age'] = 35

children_1 = dict()
children_1['name'] = 'Alice'
children_1['age'] = 6

children_2 = dict()
children_2['name'] = 'Bob'
children_2['age'] = 8
# children_2['surname'] = 'Mordis'

family_member['children'] = [children_1, children_2]

for i_children in family_member['children']:
    if i_children.get('name') == 'Bob':
        last_name = i_children.get('surname', 'Nosurname')
        print(last_name)