from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    counts = sorted(counter.values(), reverse=True)

    acc = 0
    answer = 0
    for count in counts:
        acc += count
        answer += 1
        if acc >= k:
            return answer
