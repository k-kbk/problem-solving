n = int(input())

diff = 0
time_1 = 0
time_2 = 0
last_time = 0

for _ in range(n):
    team, time = input().split()
    m, s = map(int, time.split(":"))
    now = m * 60 + s
    before_diff = diff
    diff += 1 if team == "2" else -1

    if before_diff == 0:
        last_time = now
        continue
    if diff == 0 and before_diff < 0:
        time_1 += (now) - last_time
    if diff == 0 and before_diff > 0:
        time_2 += (now) - last_time

full_time = 48 * 60
if diff < 0:
    time_1 += full_time - last_time
elif diff > 0:
    time_2 += full_time - last_time

print("%02d:%02d" % (time_1 // 60, time_1 % 60))
print("%02d:%02d" % (time_2 // 60, time_2 % 60))
