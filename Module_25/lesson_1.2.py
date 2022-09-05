class Human:

    __count = {'count': 0}

    def __init__(self, name,  age):
        self.__name = name
        self.__age = age
        self.__count['count'] += 1

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise OSError('Ошибка формата данных (данные должны быть строкой)')

    def set_age(self, age):
        if age in range(101):
            self.__age = age
        else:
            raise OSError('Ошибка формата данных (данные должны быть в диапазоне от 0 до 100)')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_count(self):
        return 'Общее количество инициализированных объектов: {}'.format(self.__count['count'])

    def __str__(self):
        return 'Имя: {}\nВозраст: {}'.format(self.__name, self.__age)


human = Human('Den', 15)
h = Human('Ferg', 35)
gdg = Human('Sofa', 26)
human.set_age(25)
human._Human__age = 48 # Не рекомендуется так делать
print(human)
print(human.get_count())



