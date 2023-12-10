N = int(input())

sharks = [list(map(int, input().split())) for _ in range(N)]
eatable_list = [list() for _ in range(N)]
eaten = [-1]*N
visited = [False]*N

for i in range(N-1) :
  ia, ib, ic = sharks[i]
  for j in range(i+1, N) :
    ja, jb, jc = sharks[j]
    if ia >= ja and ib >= jb and ic >= jc :
      eatable_list[i].append(j)
    elif ia <= ja and ib <= jb and ic <= jc :
      eatable_list[j].append(i)

def dfs(shark) :
  for other in eatable_list[shark] :
    if eaten[other] == -1 :
      eaten[other] = shark
      return True
  for other in eatable_list[shark] :
    if visited[other] :
      continue
    visited[other] = True
    if dfs(eaten[other]) :
      visited[other] = False
      eaten[other] = shark
      return True
  return False

ans = 0
for i in range(N) :
  if dfs(i) :
    ans += 1
for i in range(N) :
  if dfs(i) :
    ans += 1
print(N - ans)