goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('Текущий ассортимент:', goods)

new_fruit = input('\nНовый фрукт: ')
price = int(input('Цена: '))

goods.append([new_fruit, price])

print('\nНовый ассортимент:', goods)

for i in goods:
    i[1] = round(i[1] * 1.08, 2)
print('\nНовый ассортимент с увел. ценой:', goods)