def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


N = int(input())

for _ in range(N):
    A = int(input())
    count = 0
    while A >= 2:
        if is_prime(A):
            print(count)
            break
        count += 1
        A -= 1
    else:
        print(-1)
