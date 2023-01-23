def my_def(num, lst = []):
    lst.append(num)
    print(lst)

# number = int(input('Введите число: ' ))
my_def(5)
my_def(10)
my_def(15)

def my_def(num, lst = None):
    lst = lst or []
    # хитрая конструкция, которая позволит упростить ввод:
    # if not lst:
    #    lst = []
    # Первый вариант будет выбран, если nums не равен None, иначе будет создан и записан пустой список
    lst.append(num)
    print(lst)

my_def(5)
my_def(10)
my_def(15)