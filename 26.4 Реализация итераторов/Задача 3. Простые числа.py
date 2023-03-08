class Primes():

    def __init__(self, N):
        self.lst = range(2, N)

    def __iter__(self):
        pass

    def __next__(self):
        k = 0
        for i in range(2, N // 2 + 1):
            if (N % i == 0):
                k = k + 1
        if k <= 0:
            return i


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')