import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        answer += 1

    return -1
