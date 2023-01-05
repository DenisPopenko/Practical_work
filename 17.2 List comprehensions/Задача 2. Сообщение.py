text = input('Введите строку: ')
word = input('Введите дополнительный символ: ')

text_lst = [x * 2 for x in text]
text_lst_ = [x + word for x in text_lst]
print(f'\nСписок удвоенных символов: {text_lst}')
print(f'Склейка с дополнительным символом: {text_lst_}')

# text_lst_ = []
# for i in text:
#     text_lst_.append(i * 2 + word)
# print(text_lst_)

