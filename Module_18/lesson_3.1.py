def ceasar_chipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33]
                  if sym != ' ' else ' ')
                 for sym in string]
    new_str = ''.join(char_list)

    return new_str

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str = input('Введите строку: ').lower()
shift = int(input('Введите сдвиг: '))

output_str = ceasar_chipher(input_str, shift)

print('Зашифрованная строка:', output_str)
