def solution(brown, yellow):
    for n in range(1, yellow + 1):
        if yellow % n != 0:
            continue
        w = yellow // n
        if (2 * w) + (2 + n) * 2 == brown:
            
            return [w + 2, n + 2]
