def factorial(num):
    if num == 1:
        return 1
    fact_n_minus_1 = factorial(num - 1)
    return num * fact_n_minus_1

print(factorial(999))