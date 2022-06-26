import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = random.randint(5, 9)
a = random.randint(0, 4)
print(a, b)
nums[a:b] = []

print(nums)