from collections import deque

def bfs(si, sj):
    visited = [[0] * W for _ in range(H)]
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1

    while queue:
        ci, cj = queue.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == 0 and arr[ni][nj] == 'L':
                queue.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

    return visited[ci][cj]-1

H, W = map(int, input().split())
arr = [list(map(str, input())) for _ in range(H)]
maxV = 0

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'L':
            tmp = bfs(i, j)
            if tmp > maxV:
                maxV = tmp

print(maxV)