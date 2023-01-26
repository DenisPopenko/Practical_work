import os

# cur_path = input('Ищем в: ')
# file_name = input('Имя файла: ')

# print(os.path.abspath('Ситауция по залогам БРК на 26.01.23.docx'))

def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):
            if i_elem == file_name:
                return path
        else:
            result = find_file(path, file_name)
            if result:
                break

    return result

find_file('D:\Denis\Мои документы', 'Справка по реализации и оплате с расшифровкой по договорам 18.01.23.xlsx')