def solution(msg):
    dct = {chr(ord("A") + i): i + 1 for i in range(26)}
    idx = 27
    answer = []
    start = 0
    n = len(msg)
    while start < n:
        length = 1
        while start + length <= n and msg[start : start + length] in dct:
            length += 1
        answer.append(dct[msg[start : start + length - 1]])
        dct[msg[start : start + length]] = idx
        idx += 1
        start += length - 1

    return answer
