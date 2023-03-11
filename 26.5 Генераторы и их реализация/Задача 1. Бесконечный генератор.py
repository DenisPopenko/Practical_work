def infinite_gen():
    count = 0
    while True:
        count += 1
        yield count

# my_gen = infinite_gen()
# for i in my_gen:
#     print(i)


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for i in get_prime_numbers(50):
    print(i, end='\t')
print()