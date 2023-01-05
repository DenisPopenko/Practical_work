films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

top_films = []

while True:
    print('\nВаш текущий топ фильмов:', top_films)
    film = input('Название фильма: ')
    print('Команды: добавить, вставить, удалить')
    command = input('Введите команду: ')
    if command == 'добавить':
        # if exist(film, top_films):
        #     print('Такой фильм уже в списке.')
        # else:
        top_films.append(film)
    elif command == 'вставить':
        index = int(input('На какое место? ')) - 1
        top_films.insert(index, film)
    elif command == 'удалить':
        top_films.remove(film)
