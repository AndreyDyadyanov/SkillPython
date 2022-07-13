def factorial(number):
    if number == 1:
        return 1
    result = factorial(number - 1)
    return number * result

number = int(input('Введите число: '))

print(factorial(number))