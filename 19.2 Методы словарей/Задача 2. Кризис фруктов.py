incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

print('Общий доход за год составил {} рублей'.format(sum(incomes.values())))

def get_key(d):
    min_d = min(d.values())
    for k, v in d.items():
        if v == min_d:
            return(k)

print('Самый маленький доход у {}. Он составляет {} рублей'.
      format(get_key(incomes), min(incomes.values())))
incomes.pop(get_key(incomes))
print('Итоговый словарь:', incomes)