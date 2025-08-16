from collections import Counter


def solution(topping):
    left = set()
    right = Counter(topping)
    answer = 0
    for t in topping:
        left.add(t)
        right[t] -= 1
        if right[t] == 0:
            del right[t]

        if len(left) == len(right):
            answer += 1

    return answer
