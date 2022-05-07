while True:
    operation = input('Выберете операцию: ')
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        break
    else:
        print('Ошибка: такой операции не существует. Попробуйте еще раз.')
        
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if operation == '+':
    c = a + b
    print(a, '+', b, '=', c)
elif operation == '-':
    c = a - b
    print(a, '-', b, '=', c)
elif operation == '*':
    c = a * b
    print(a, '*', b, '=', c)
elif operation == '/':
    c = a / b
    print(a, '/', b, '=', c)


