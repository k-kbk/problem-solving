from collections import Counter

T = int(input())

for _ in range(T):
    n = int(input())
    types = [input().split()[1] for _ in range(n)]
    counter = Counter(types)
    count = 1
    for key in counter:
        count *= counter[key] + 1

    print(count - 1)
