from collections import defaultdict, deque
import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7

N, M = map(int, input().split())
visited = [False]*(N+1)
edge_dict = defaultdict(list)

def bfs(start) :
    visited[start] = True
    cnt = 1
    q = deque([start])
    while q :
        node = q.popleft()
        for nxt in edge_dict[node] :
            if not visited[nxt] :
                cnt += 1
                visited[nxt] = True
                q.append(nxt)
    return cnt

def init() :
    for _ in range(M) :
        a, b = map(int, input().split())
        edge_dict[a].append(b)
        edge_dict[b].append(a)

def solve() :
    result = 1
    for i in range(1, N+1) :
        if not visited[i] :
            result = (result * bfs(i)) % MOD
    print(result)
    
if __name__ == "__main__" :
    init()
    solve()