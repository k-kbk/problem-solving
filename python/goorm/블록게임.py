from collections import deque

N = int(input())
D = input()
S = list(map(int, input().split()))

direction = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

position = deque([(0, 0)])
score = deque([1])

for i in range(N):
    dx, dy = direction[D[i]]
    x, y = position[-1]
    next_pos = (x + dx, y + dy)

    if next_pos in position:
        while True:
            score.pop()
            if position.pop() == next_pos:
                break

    position.append(next_pos)
    prev_score = score[-1] if score else 0
    score.append(prev_score + S[i])

print(score[-1])
