import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    valid = []

    N = int(input())
    numbers = list(map(int, input().split(" ")))

    counter = Counter(numbers)

    for key in counter:
        if counter[key] == 6:
            valid.append(key)

    players = []

    for n in numbers:
        if n in valid:
            players.append(n)

    d = defaultdict(list)

    for i in range(len(players)):
        d[players[i]].append(i + 1)

    print(sorted(d, key=lambda x: (sum(d[x][0:4]), d[x][4]))[0])
