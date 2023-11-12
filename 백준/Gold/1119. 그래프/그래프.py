import sys
input = sys.stdin.readline

N = int(input())
maps = [input().strip() for _ in range(N)]

if N == 1 :
  print(0)
  exit()

visited = [False]*N
edge_list = list()

def dfs(node) :
  q = [ node ]
  visited[node] = True
  edges, nodes = 0, 0

  while q :
    node = q.pop()
    nodes += 1
    for i in range(N) :
      if maps[node][i] == 'N' :
        continue
      edges += 1
      if not visited[i] :
        visited[i] = True
        q.append(i)
  edge_list.append((nodes, edges // 2))

for i in range(N) :
  if not visited[i] :
    dfs(i)

enable = True
cnt = 0
for nodes, edges in edge_list :
  if nodes == 1 :
    enable = False
    break
  cnt += edges - nodes + 1

print(len(edge_list) - 1 if enable and cnt >= len(edge_list)-1 else -1)