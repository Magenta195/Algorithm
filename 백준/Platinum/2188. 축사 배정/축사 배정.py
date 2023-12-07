import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rooms = [-1]*(M+1)
cows = [list() for _ in range(N)]

for i in range(N) :
  _, *room = map(int, input().split())
  cows[i] = room

def dfs(node) :
  if visited[node] :
    return False
  visited[node] = True
  for room in cows[node] :
    if rooms[room] == -1 or dfs(rooms[room]) :
      rooms[room] = node
      return True
  return False

result = 0
for i in range(N) :
  visited = [False]*(N+1)
  if dfs(i) :
    result += 1
print(result)