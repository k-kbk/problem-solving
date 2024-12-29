import sys

input = sys.stdin.readline

p, m = map(int, input().split(" "))

rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    isEntered = False

    for room in rooms:
        if len(room) < m and abs(room[0][0] - l) <= 10:
            room.append((l, n))
            isEntered = True
            break

    if not isEntered:
        rooms.append([(l, n)])

for room in rooms:
    room.sort(key=lambda x: x[1])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    for l, n in room:
        print(l, n)
