from collections import Counter

_ = input()
nums = input().split()
counter = Counter(nums)

arr = []

for item in counter.most_common():
    arr.append([item[0], item[1], nums.index(item[0])])

sorted(arr, key=lambda x: (x[1], x[2]))

for item in arr:
    print(f"{item[0]} " * int(item[1]), end="")
