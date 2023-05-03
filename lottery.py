import random

nums = []

for i in range(0,6):
    num = random.randint(1,50)
    while num in nums:
        num = random.randint(1,50)

    nums.append(num)

nums.sort()
print(nums)