import random

original_prices = [random.randint(-50, 100) for _ in range(5)]

new_prices = original_prices[:]

new_prices = [(x if x > 0 else 0) for x in new_prices]

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))