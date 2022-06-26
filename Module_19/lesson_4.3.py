line = input('Введите строку: ')

new_line = set(line)

different_number = [number for number in new_line if '0' <= number <= '9']



print('Различные цифры строки {}'.format(''.join(different_number)))