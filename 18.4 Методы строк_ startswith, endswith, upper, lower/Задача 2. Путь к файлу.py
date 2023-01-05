path = input('Путь к файлу: ',) # C:/user/docs/folder/new_file.txt
disk = input('На каком диске должен лежать файл: ').lower()
expansion = input('Требуемое расширение файла: ')

if not path.endswith(expansion):
    print('Не верно указано расширение!')
elif not path.startswith(disk):
    print('Не верно указан диск!')
else:
    print('Путь корректен!')