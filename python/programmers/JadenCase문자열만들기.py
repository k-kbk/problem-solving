def solution(s):
    result = []
    is_start = True

    for ch in s.lower():
        if is_start:
            result.append(ch.upper())
        else:
            result.append(ch)
        is_start = ch == " "

    return "".join(result)
