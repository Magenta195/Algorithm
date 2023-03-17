from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = 0, 0

def init(board) :
    global N, M
    N, M = len(board), len(board[0])
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 'R' :
                start = (j, i)
            if board[i][j] == 'G' :
                end = (j, i)
                
    return start, end

def move(board, x, y, k) :
    while -1 < x < M and -1 < y < N and board[y][x] != 'D':
        x, y = x + dx[k], y + dy[k]
    
    return x - dx[k], y - dy[k]

def bfs(board, start, end) :
    x, y = start
    q = deque([(x, y, 0)])
    visited = [[float('inf')]*M for _ in range(N)]
    visited[y][x] = 0
    
    while q :
        x, y, dist = q.popleft()
        if (x, y) == end :
            return dist
        
        for k in range(4) :
            ax, ay = move(board, x, y, k)
            if visited[ay][ax] > dist + 1 :
                visited[ay][ax] = dist + 1
                q.append((ax, ay, dist+1))

    return -1
    
def solution(board):
    start, end = init(board)
    result = bfs(board, start, end)

    return result