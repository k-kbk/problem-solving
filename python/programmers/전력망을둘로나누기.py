from collections import defaultdict, deque


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)

    return count


def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        graph = defaultdict(list)
        for j in range(len(wires)):
            if i == j:
                continue
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = [False] * (n + 1)
        count = bfs(1, graph, visited)
        diff = abs(n - count - count)
        answer = min(answer, diff)

    return answer
