line = (1, 2, 3, 'jhk', 5, 17, 'ss')

result = []

if isinstance(line, dict):
    line = list(line.values())

    for index, element in enumerate(line):
        if index % 2 == 0:
            result.append(element)

else:
    for index, element in enumerate(line):
        if index % 2 == 0:
            result.append(element)

print('Результат: {}'.format(result))