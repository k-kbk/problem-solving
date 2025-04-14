def solution(sizes):
    max_w = 0
    max_h = 0
    for w, h in sizes:
        max_len = max(w, h)
        min_len = min(w, h)
        max_w = max(max_len, max_w)
        max_h = max(min_len, max_h)
        
    return max_w * max_h
