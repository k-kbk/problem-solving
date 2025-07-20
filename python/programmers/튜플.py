def solution(s):
    s = s[2:-2]
    sets = s.split("},{")
    parsed = [list(map(int, group.split(","))) for group in sets]
    parsed.sort(key=len)

    answer = []
    prev = set()

    for group in parsed:
        curr = set(group)
        diff = curr - prev
        answer.append(next(iter(diff)))
        prev = curr

    return answer
