def play(n, board, r, c):
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True
    score = 1

    while True:
        order = board[r][c]
        count = int(order[:-1])
        d_r, d_c = directions[order[-1]]

        for _ in range(count):
            r, c = (r + d_r) % n, (c + d_c) % n
            if visited[r][c]:
                return score
            visited[r][c] = True
            score += 1


N = int(input())
g_r, g_c = map(int, input().split())
p_r, p_c = map(int, input().split())
board = [list(input().split()) for _ in range(N)]

g_score = play(N, board, g_r - 1, g_c - 1)
p_score = play(N, board, p_r - 1, p_c - 1)

print(f"goorm {g_score}" if g_score > p_score else f"player {p_score}")
