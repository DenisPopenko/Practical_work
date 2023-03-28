def counter(func):
    '''
    Декоратор-счётчик
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):
        global count
        count += 1
        result = func(*args, **kwargs)
        print('Функция {} была вызвана: {} раз'.format(func.__name__, count))

        return result

    wrapper.count = 0
    return wrapper


# Функция, вызовы которой нужно считать

count = 0
@counter
def test():
    print("Привет, Маша!")


test()
test()
test()

def counter(func):
    count = 0
    '''
    Декоратор-счётчик
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print('Функция {} была вызвана: {} раз'.format(func.__name__, count))

        return result

    wrapper.count = 0
    return wrapper


# Функция, вызовы которой нужно считать

@counter
def test():
    print("Привет, Маша!")


test()
test()
test()
print(dir())