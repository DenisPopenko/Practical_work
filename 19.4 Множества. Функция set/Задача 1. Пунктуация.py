symbols = set(".,;:!?")
lst = input('Введите строку: ')
count = 0

for i in lst:
    if i in symbols:
        count += 1
print(count)