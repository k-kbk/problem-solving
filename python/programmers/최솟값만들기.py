def solution(A, B):
    return sum(map(lambda x: x[0] * x[1], zip(sorted(A), sorted(B, reverse=True))))
