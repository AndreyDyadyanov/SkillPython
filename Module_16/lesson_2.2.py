def search_symbol(message):
    symbol_list = list(message)
    symbol_count = symbol_list.count('!') + symbol_list.count('?')

    return symbol_count

def print_message(message_1, message_2):
    message = []
    message.extend(message_1)
    message.extend(message_2)
    for p_message in message:
        print(p_message, end=(''))



first_message = input('Первое сообщение: ')
second_message = input('Второе сообщение: ')

if search_symbol(first_message) > search_symbol(second_message):
    print_message(first_message, second_message)
elif search_symbol(second_message) > search_symbol(first_message):
    print_message(second_message, first_message)
else:
    print('Ой')
