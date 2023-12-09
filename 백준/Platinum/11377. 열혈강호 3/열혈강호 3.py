import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

work_list = [list(map(int, input().split()))[1:] for _ in range(N)]

work = [-1]*(M+1)
ans = 0

def dfs(node) :
  if visited[node] : 
    return False
  visited[node] = True

  for w in work_list[node] :
    if work[w] == -1 :
      work[w] = node
      return True
  for w in work_list[node] :
    if dfs(work[w]) :
      work[w] = node
      return True
  return False

res_0, res_1 = 0, 0
for i in range(N) :
  visited = [False]*N
  if dfs(i) :
    res_0 += 1
  if res_0 == M :
    break

for i in range(N) :
  visited = [False]*N
  if dfs(i) :
    res_1 += 1
  if res_0 + res_1 == M or res_1 == K :
    break

print(res_0 + res_1)