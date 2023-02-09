str = input('Введите строку: ')
try:
    file = open('res', 'w')
    file.write(str)
except FileExistsError:
    print('Проблема при открытии файла')
except ValueError:
    print('Нельзя преобразовать данные в целое')
except:
    print('Неожиданная ошибка')
else:
    print('Программа выполнилась без ошибок')
finally:
    file.close()
