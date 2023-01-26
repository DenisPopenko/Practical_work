import os

path = input('Путь: ')

if not os.path.exists(path):
    print('Указанного пути не существует')
else:
    if os.path.isdir(path):
        print('Это директория')
    elif os.path.islink(path):
        print('Это ссылка')
    elif os.path.isfile(path):
        print(F'Это файл\nРазмер файла: {os.path.getsize(path)} байт')
