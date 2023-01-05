import random
original_prices = [random.randint(-12, 5) for price in range(5)]
#print(original_prices)
new_prices = original_prices[:]
original_prices = [x if x > 0 else 0 for x in original_prices]
#print((original_prices))
#print((new_prices))
print("Мы потеряли:",  sum(original_prices) - sum(new_prices))