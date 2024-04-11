import math

n = int(input())

answer = "long int"

while True:
    n -= 4
    if n <= 0:
        break

    answer = "long " + answer

print(answer)
