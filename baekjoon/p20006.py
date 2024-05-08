import sys

input = sys.stdin.readline

p, m = map(int, input().split(" "))

rooms = []

for _ in range(p):
    level, id = input().split()
    level = int(level)

    isEntered = False

    for room in rooms:
        if len(room) < m and abs(room[0][0] - level) <= 10:
            room.append((level, id))
            isEntered = True
            break

    if not isEntered:
        rooms.append([(level, id)])

for room in rooms:
    room.sort(key=lambda x: x[1])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    for level, id in room:
        print(level, id)
