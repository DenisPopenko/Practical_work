import random

first = [random.randint(50, 80) for number in range(10)]
second = [random.randint(30, 60) for number in range(10)]

third_squad = ["Погиб" if first[i] + second[i] > 100 else "Выжил" for i in range(10)]

print("Урон первого отряда:", first)
print("Урон второго отряда:", second)
print("Состояние третьего отряда:", third_squad)
