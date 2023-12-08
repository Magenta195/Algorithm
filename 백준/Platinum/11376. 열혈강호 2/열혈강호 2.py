import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
worker_list = [tuple(map(int, input().split()))[1:] for _ in range(N)]
works = [-1]*(M+1)
ans = 0

def dfs(worker) :
  if visited[worker] :
    return False
  visited[worker] = True

  for work in worker_list[worker] :
    if works[work] == -1 :
      works[work] = worker
      return True
  for work in worker_list[worker] :
    if dfs(works[work]) :
      works[work] = worker
      return True
  return False

for i in range(N) :
  visited = [False]*N
  if dfs(i) :
    ans += 1
  visited = [False]*N
  if dfs(i) :
    ans += 1
  if ans == M :
    break

print(ans)