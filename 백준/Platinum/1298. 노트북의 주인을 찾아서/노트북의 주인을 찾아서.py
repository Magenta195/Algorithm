import sys
input = sys.stdin.readline

N, M = map(int, input().split())
choose_list = [list() for _ in range(N+1)]
laptops = [0]*(N+1)
visited = [False]*(N+1)
ans = 0
for _ in range(M) :
  a, b = map(int, input().split())
  choose_list[a].append(b)

def dfs(man) :
  for i in choose_list[man] :
    if not laptops[i] :
      laptops[i] = man
      return True
  for i in choose_list[man] :
    if visited[i] :
      continue
    visited[i] = True
    if dfs(laptops[i]) :
      laptops[i] = man
      visited[i] = False
      return True

for i in range(1, N+1) :
  if dfs(i) :
    ans += 1
print(ans)