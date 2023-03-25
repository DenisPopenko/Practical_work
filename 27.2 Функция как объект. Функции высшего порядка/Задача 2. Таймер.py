import time

def timer(func, *args, **kwargs):
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_at, 4)
    return run_time, result
def func_2(func, *args, **kwargs):
    result = func(*args, **kwargs) * func(*args, **kwargs)
    return result


def func_1(x):
    return x + 10

my_time = timer(func_1, 9)
print(my_time)