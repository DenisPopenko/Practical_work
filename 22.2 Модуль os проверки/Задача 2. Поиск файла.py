import os

# cur_path = input('Ищем в: ')
# file_name = input('Имя файла: ')

cur_path = 'D:\skillbox\dpo_python_basic'
file_name = 'main.py'

# print(os.path.abspath('Ситауция по залогам БРК на 26.01.23.docx'))

def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):
            if i_elem == file_name:
                print(path)
        else:
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result

print(find_file(cur_path, file_name))
