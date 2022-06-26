def histogram(string):
    text_dict = dict()
    for symbol in string:
        if symbol in text_dict:
            text_dict[symbol] += 1
        else:
            text_dict[symbol] = 1

    return text_dict





text = input('Введите текст: ')

hist = histogram(text)


for symbol in sorted(hist.keys()):
    print('{0} : {1}'.format(symbol, hist[symbol]))

print('Максимальная частота: {}'.format(max(hist.values())))