def func_2(func, *args, **kwargs):
    result = func(*args, **kwargs) * func(*args, **kwargs)
    return result


def func_1(x):
    return x + 10


print(func_2(func_1, 9))