def solution(prices):
    answer = []
    length = len(prices)
    for i in range(length):
        t = 0
        for j in range(i + 1, length):
            t += 1
            if prices[j] < prices[i]:
                break
        answer.append(t)

    return answer
