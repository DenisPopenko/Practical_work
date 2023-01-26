import os

def print_dir(project):
    print('\nСодержимое каталога:', project)
    for i_elem in os.listdir(project):
        path = os.path. join(project, i_elem)
        print('     ', path)

catalog = 'dpo_python_basic'
path_to_catalog = os.path.abspath(os.path.join('..', '..', catalog))
print_dir(path_to_catalog)

# или

for path in os.listdir('..'):
    print(os.path.join(os.path.abspath('..'), path))

