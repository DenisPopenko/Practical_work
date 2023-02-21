class DivisionError(Exception):

    pass



with open('numbers.txt', 'r') as file:
    s = []
    try:
        for i in file:
            s.append(int(i))
        if s[0] < s[1]:
            raise DivisionError('Нельзя делить меньшее на большее')
    except:
        print('Нельзя делить меньшее на большее')
    print(s[0] / s[1])

