import sys
input = sys.stdin.readline

dy = [-1, 0, 1]

R, C = map(int, input().split())
map_list = [input().strip() for _ in range(R)]
visited = [[False]*C for _ in range(R)]

def dfs(idx, y) :
  if idx == C - 1 :
    return True

  for k in range(3) :
    ay = y + dy[k]
    if -1 < ay < R and map_list[ay][idx+1] != 'x' and not visited[ay][idx+1] :
      visited[ay][idx+1] = True
      is_enable = dfs(idx+1, ay)
      if is_enable :
        return True

  return False

result = 0
for r in range(R) :
  if map_list[r][0] != 'x' :
    visited[r][0] = True
    is_enable = dfs(0, r)
    if is_enable :
      result += 1

print(result)