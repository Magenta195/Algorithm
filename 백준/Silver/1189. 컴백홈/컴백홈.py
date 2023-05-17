R, C, K = map(int, input().split())

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

visited = [[False]*C for _ in range(R)]

map_list = [input().strip() for _ in range(R)]

def dfs(r, c, k) :
  if r == 0 and c == C-1 :
    return 1 if  k == 0 else 0
  if k == 0 :
    return 0
    
  result = 0
  for i in range(4) :
    ar, ac = r + dr[i], c + dc[i]
    if -1 < ar < R and -1 < ac < C and map_list[ar][ac] == '.' and not visited[ar][ac] :
      visited[ar][ac] = True
      result += dfs(ar, ac, k-1)
      visited[ar][ac] = False

  return result

visited[R-1][0] = True
print(dfs(R-1, 0, K-1))