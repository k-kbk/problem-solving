T = int(input())
answer = 0

for _ in range(T):
    A, B = map(int, input().split())
    min_num = min(A, B)
    if min_num * 1.6 <= max(A, B) <= min_num * 1.63:
        answer += 1

print(answer)
