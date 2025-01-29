import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

target = input().strip()
tc = Counter(target)

result = 0

for i in range(n - 1):
    word = input().strip()
    wc = Counter(word)

    c1 = tc - wc
    c2 = wc - tc

    if len(c1) == 0 and len(c2) == 0:
        result += 1
        continue

    elif len(c1) == 1 and sum(c1.values()) == 1 and len(c2) == 0:
        result += 1
        continue

    elif len(c2) == 1 and sum(c2.values()) == 1 and len(c1) == 0:
        result += 1
        continue

    elif sum(c1.values()) == 1 and sum(c2.values()) == 1:
        result += 1

print(result)
