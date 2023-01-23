def sum_range(n):
    if n <= 0:
        return
    sum_range(n - 1)
    print(n)

num = int(input('Введите num: '))
sum_range(num)