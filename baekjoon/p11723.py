import sys

m = int(sys.stdin.readline())

s = set()

for i in range(m):
    line = sys.stdin.readline().strip()

    if line == "all":
        s = set([i for i in range(1, 21)])
        continue
    if line == "empty":
        s = set()
        continue

    command, n = line.split(" ")
    n = int(n)

    if command == "add":
        s.add(n)
    if command == "remove":
        s.discard(n)
    if command == "check":
        print(1 if n in s else 0)
    if command == "toggle":
        if n in s:
            s.discard(n)
        else:
            s.add(n)
