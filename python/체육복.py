def solution(n, lost, reserve):
    
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    
    for k in sorted(r):
        if (k - 1) in l:
            l.remove(k - 1)
        elif (k + 1) in l:
            l.remove(k + 1)
    
    return n - len(l)