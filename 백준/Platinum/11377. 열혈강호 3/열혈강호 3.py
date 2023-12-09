import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
work_list = []
for _ in range(N):
  n, *lst = map(int, input().split())
  if not n:
    N -= 1
  else:
    work_list.append(lst)
work = [-1] * (M + 1)
visited = [False] * N
ans = 0

def dfs(node):
  for w in work_list[node]:
    if work[w] == -1:
      work[w] = node
      return True
  for w in work_list[node]:
    if visited[work[w]]:
      continue
    visited[work[w]] = True
    if dfs(work[w]) :
      visited[work[w]] = False
      work[w] = node
      return True
  return False

res_0, res_1 = 0, 0
for i in range(N):
  if dfs(i):
    res_0 += 1
  if res_0 == M:
    break

for i in range(N):
  if len(work_list[i]) == 1:
    continue
  if dfs(i):
    res_1 += 1
  if res_0 + res_1 == M or res_1 == K:
    break
print(res_0 + res_1)