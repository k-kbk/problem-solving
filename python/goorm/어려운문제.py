import math


def spread(n):
    return list(str(n))


num = math.factorial(int(input()))
nums = spread(num)
while len(nums) != 1:
    nums = spread(sum(map(int, nums)))

print(nums[0])
