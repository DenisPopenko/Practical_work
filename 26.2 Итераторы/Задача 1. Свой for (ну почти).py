h = [10, 20, 30]
iterator = iter(h)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# for i in h:
#     print(i)
