word_list = []
word_count = [0, 0, 0]

for i in range(3):
    print('Введите', i + 1, 'слово:', end=' ')
    word = input()
    word_list.append(word)

print()
text = input('Слово из текста: ')

while text != 'end':
    for index in range(3):
        if text == word_list[index]:
            word_count[index] += 1

    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')
for i in range(3):
    print(str(word_list[i]) + ':', word_count[i])
