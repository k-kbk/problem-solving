import sys

N, K = list(map(int, sys.stdin.readline().strip().split(" ")))

countries = list()

for i in range(N):
    countries.append(list(map(int, sys.stdin.readline().strip().split(" "))))

countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(len(countries)):
    if countries[i][0] == K:
        if i == 0:
            result = i + 1
        else:
            count = 0
            while True:
                prev = "".join(map(str, countries[i - count - 1][1:]))
                now = "".join(map(str, countries[i][1:]))

                if now == prev:
                    count += 1
                else:
                    result = i + 1 - count
                    break
        break

print(result)
