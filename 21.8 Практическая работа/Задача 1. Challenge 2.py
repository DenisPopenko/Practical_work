# num = int(input('Введите num: '))
def sum_range(n, k = 0):
    k += 1
    if k == n:
        return n
    return sum_range(k)



print(sum_range(10))

# for i in range(1, 11):
#     print(i)
