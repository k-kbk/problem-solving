from collections import Counter


def solution(clothes):
    answer = 1
    counter = Counter(type for _, type in clothes)
    for count in counter.values():
        answer *= count + 1

    return answer - 1
