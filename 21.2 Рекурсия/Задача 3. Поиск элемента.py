site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search_value(struct, key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = search_value(sub_struct, key)
            if result:
                break

    else:
        result = 'Такого ключа в структуре сайта нет'

    return result




key = input('Искомый ключ: ')
print('Значение:', search_value(site, key))


# Пример 1:
#
# Искомый ключ: h2
# Значение: Здесь будет мой заголовок
#
# Пример 2:
#
# Искомый ключ: abc
# Такого ключа в структуре сайта нет.

