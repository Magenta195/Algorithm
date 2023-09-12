import sys
input = sys.stdin.readline

MAX = float('inf')

N, S, E, M = map(int, input().split())
edge_list = [[-MAX]*N for _ in range(N)]
for _ in range(M) :
  a, b, c = map(int, input().split())
  edge_list[a][b] = max(edge_list[a][b], -c)
money_list = list(map(int, input().split()))
for i in range(N) :
  for j in range(N) :
    edge_list[i][j] += money_list[j]
dist_list = [-MAX]*N
dist_list[S] = money_list[S]

visited = [False]*N
def dfs(x) :
  if x == E :
    return True
  for i in range(N) :
    if edge_list[x][i] > -MAX and not visited[i] :
      visited[i] = True
      tmp = dfs(i)
      visited[i] = False
      if tmp :
        return True
  return False

for _ in range(N) :
  for i in range(N) :
    for j in range(N) :
      if edge_list[j][i] > -MAX and dist_list[i] < dist_list[j] + edge_list[j][i] :
        dist_list[i] = dist_list[j] + edge_list[j][i]
if dist_list[E] == -MAX :
  print("gg")
  exit()
for i in range(N) :
  for j in range(N) :
    if edge_list[j][i] > -MAX and dist_list[i] < dist_list[j] + edge_list[j][i] :
      if dfs(i) :
        print("Gee")
        exit()

print(dist_list[E])