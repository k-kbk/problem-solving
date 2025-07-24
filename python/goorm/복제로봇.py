position = tuple(map(int, input().split()))
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
C = input().split()
directions = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

for command in C:
    x, y = position
    d_x, d_y = directions[command]
    new_position = (x + d_x, y + +d_y)
    if not new_position in XY:
        position = new_position

print(position[0], position[1])
