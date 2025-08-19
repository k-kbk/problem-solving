N = int(input())
count = 0

for heal in [14, 7, 1]:
    count += N // heal
    N = N % heal

print(count)
