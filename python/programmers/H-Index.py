def solution(citation):
    answer = 0
    citation.sort()
    ls_len = len(citation)
    for h in range(ls_len, 0, -1):
        count = len([c for c in citation if c >= h])
        if count >= h and ls_len - count <= h:
            answer = h
            break

    return answer