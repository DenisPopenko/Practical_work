word = input('Введите строку: ')
index = int(input('Номер символа: '))

print()

word_list = list(word)
count = 0
if index - 1 > 0:
    print('\nСимвол слева:', word_list[index - 2])
    if word_list[index - 1] == word_list[index - 2]:
        count += 1
if index - 1 < len(word) - 1:
    print('Символ справа:', word_list[index])
    if word_list[index - 1] == word_list[index]:
        count += 1

if count == 1:
    print('\nЕсть ровно один такой же символ.')
elif count == 2:
    print('\nЕсть два таких же символа.')
else:
    print('\nТаких же символов нет.')