print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])
print([value for i_key, value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])

# data = {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}
# for i, j in data.items():
#     if i % 2 == 0:
#         print(j, end = ' ')