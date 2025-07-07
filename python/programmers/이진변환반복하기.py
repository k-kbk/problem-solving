def solution(s):
    cnt, zeros = 0, 0
    while s != '1':
        zeros += s.count('0')
        s = bin(len(s.replace('0', '')))[2:]
        cnt += 1
        
    return [cnt, zeros]
