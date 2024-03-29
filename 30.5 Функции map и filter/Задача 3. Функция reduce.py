import functools

sentences = ["Nory was a Catholic", "because her mother was a Catholic",
             "and Nory’s mother was a Catholic", "because her father was a Catholic",
             "and her father was a Catholic", "because his mother was a Catholic", "or had been"]


def check_was(a, b):
    if isinstance(a, str):  # обработаем первый элемент отдельно
        a = int(a.count('was'))
    result = a + int(b.count('was'))
    return result  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка


print(functools.reduce(check_was, sentences))