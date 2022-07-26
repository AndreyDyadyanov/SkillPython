def is_palindrome(line):
    palindrom = {}

    for i_sym in set(line):
        palindrom[i_sym] = line.count(i_sym)

    count = 0

    for i_num in palindrom.values():
        if i_num % 2 != 0:
            count += 1

    if count <= 1:
        return 1
    else:
        return 0

palindrome_count = 0

file = open('words.txt', 'r')
errors_file = open('errors.log', 'w')
try:
    for word in file:
        clear_word = word.replace('\n', '')
        if clear_word.isalpha():
            count = is_palindrome(clear_word)
            palindrome_count += count
        else:
            errors_file.write('ValueError: the program found a number in the file "words.txt"')
            raise ValueError
except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    raise ValueError('Прорамма обнаружила число')

finally:
    print('Количество слов из которых можно сделать палиндром: {}'.format(palindrome_count))
    file.close()
    errors_file.close()

