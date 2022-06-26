word_list = []
word_count = [0, 0, 0]

for i in range(3):
    print('Введите', i + 1, 'слово:', end=' ')
    word = input()
    word_list.append(word)

print()

text = input('Введите текст: ').split()

for i in range(3):
    word_count[i] = text.count(word_list[i])

print('\nПодсчёт слов в тексте')
for i in range(3):
    print(str(word_list[i]) + ':', word_count[i])