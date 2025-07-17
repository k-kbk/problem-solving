from functools import cmp_to_key


def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


def solution(numbers):
    ls = list(map(str, numbers))
    numbers_sorted = sorted(ls, key=cmp_to_key(compare))
    answer = "".join(numbers_sorted)
    return "0" if answer[0] == "0" else answer
