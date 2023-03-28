from typing import List
# Введите числа: 5 8 4 1 0 3
# [0, 1, 3, 4, 5, 8]


print(sorted(list(map(int, input('Введите числа: ').split()))))