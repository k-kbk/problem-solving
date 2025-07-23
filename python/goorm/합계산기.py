import math

T = int(input())
answer = 0

for _ in range(T):
    answer += math.floor(eval(input()))

print(answer)
