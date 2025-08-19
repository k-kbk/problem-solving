N = int(input())
events = [list(map(int, input().split())) for _ in range(N)]
time = 0
count = 0

while events:
    events = [e for e in events if e[0] > time]
    if not events:
        break
    end = min(e[1] for e in events)
    time = end
    count += 1

print(count)
