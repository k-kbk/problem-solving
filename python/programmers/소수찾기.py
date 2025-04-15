from itertools import permutations

def solution(numbers):
    answer = set()
    nums = list(numbers)
    for i in range(1, len(nums) + 1):
        for p in permutations(nums, i):
            num = int("".join(p))
            if isprime(num):
                answer.add(num)
    return len(answer)

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
