def search_film(film, films_list):
    for search in films_list:
        if search == film:
            return True

    return False



films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

user_list = []

while True:
    print('\nВаш текущий топ фильмов:', user_list)
    film = input('Название фильма: ')
    if search_film(film, films):
        print('Команды: добавить, вставить, удалить')
        commands = input('Введите команду: ')

        if commands == 'добавить':
            if search_film(film, user_list):
                print('Этот фильм уже есть в вашем списке')
            else:
                user_list.append(film)

        if commands == 'удалить':
            if search_film(film, user_list):
                user_list.remove(film)
            else:
                print('Такого фильма нет в вашем списке.')

        if commands == 'вставить':
            place = int('На какое место в вашем рейтинге поставить фильм? ')
            user_list.insert(place, film)

    else:
        print('Такого фильма нет на сайте.')