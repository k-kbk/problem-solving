def is_not_prime(n):
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return True
    return False


N = int(input())

for _ in range(N):
    A = int(input())
    if A > 2 and is_not_prime(A):
        print("No")
    else:
        print("Yes")
