N = int(input())
count = 0
div = 5

while N >= div:
    count += N // div
    div *= 5

print(count)
