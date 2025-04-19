from collections import deque

def is_valid(visited, maps, n, m, y, x):
    return 0 <= y < n and 0 <= x < m and maps[y][x] and not visited[y][x]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0, 1)])
    visited[0][0] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        y, x, count = q.popleft()
        if (y, x) == (n - 1, m - 1):
            return count
        for dy, dx in directions:
            next_y = y + dy
            next_x = x + dx
            if is_valid(visited, maps, n, m, next_y, next_x):
                q.append((next_y, next_x, count + 1))
                visited[next_y][next_x] = True
    
    return -1
