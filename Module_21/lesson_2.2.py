data = {5, 6, 7}

print(f'Введите данные: {data}')

if isinstance(data, str):
    print(f'\nТип данных: str(строка) \nНеизменемый (immutable) \nID объекта: {id(data)}')

elif isinstance(data, int):
    print(f'\nТип данных: int(целое число) \nНеизменемый (immutable) \nID объекта: {id(data)}')

elif isinstance(data, float):
    print(f'\nТип данных: float(вещественное число) \nНеизменемый (immutable) \nID объекта: {id(data)}')

elif isinstance(data, tuple):
    print(f'\nТип данных: tuple(кортеж) \nНеизменемый (immutable) \nID объекта: {id(data)}')

elif isinstance(data, bool):
    print(f'\nТип данных: bool(булевая переменная) \nНеизменемый (immutable) \nID объекта: {id(data)}')

elif isinstance(data, list):
    print(f'\nТип данных: list(список) \nИзменемый (mutable) \nID объекта: {id(data)}')

elif isinstance(data, dict):
    print(f'\nТип данных: dict(словарь) \nИзменемый (mutable) \nID объекта: {id(data)}')

elif isinstance(data, set):
    print(f'\nТип данных: set(множество) \nИзменемый (mutable) \nID объекта: {id(data)}')

# {'a': 10, 'b': 20}