quantity = int(input('Кол-во пакетов: '))

pack = []
decoded = []
losed = 0

for i_pack in range(1, quantity + 1):
    print('\nПакет номер', i_pack)
    for i_bit in range(1, 5):
        print(i_bit, 'бит: ', end = '')
        num = int(input())
        pack.append(num)
    if pack.count(-1) >= 2:
        print('Много ошибок в пакете.')
        losed += 1
        pack = []
    else:
        decoded.extend(pack)

print('\nПолученное сообщение:', decoded)
print('Кол-во ошибок в сообщении:', decoded.count(-1))
print('Кол-во потерянных пакетов:', losed)



