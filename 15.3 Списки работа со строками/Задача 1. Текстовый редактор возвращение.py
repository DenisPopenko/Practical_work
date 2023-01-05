text = input('Введите текст: ')
list_text = list(text)

count = 0
new_text = ''
for i in list_text:
    if i == ':':
        i = ';'
        count += 1
    new_text += i

print('Исправленная строка:', new_text)
print('Кол-во замен:', count)