import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
list_a = []
list_b = []

for size_a, size_b in zip(a, b):
    list_a.extend(list(range(size_a - 2, size_a + 3)))
    list_b.extend(list(range(size_b - 2, size_b + 3)))

a = sorted(list(Counter(list_a).items()), key=lambda x: (-x[1], x[0]))
b = sorted(list(Counter(list_b).items()), key=lambda x: (-x[1], x[0]))
value_a = a[0][0]
value_b = b[0][0]

print(value_a, value_b)
print("good" if value_a > value_b else "bad")
