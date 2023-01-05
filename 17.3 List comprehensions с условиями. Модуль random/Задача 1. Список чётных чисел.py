first = int(input("Первое число А: "))
second = int(input("Второе число B: "))

result = [number for number in range(first, second + 1) if number % 2 == 0]
print(result)