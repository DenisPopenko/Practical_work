pattern = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
name = input('Список людей через запятую: ').split(', ')
age = input('Возраст людей через пробел: ').split()
# int_age = [int(i) for i in age.split()]
# print(int_age)
for i in range(len(name)):
    print(pattern.format(name = name[i], age = age[i]))

print('\nИменинники: ', ', '.join([' '.join([name[i], age[i]]) for i in range(len(name))]))