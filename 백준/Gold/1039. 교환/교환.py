N, K = input().split()
N = list(N)
M = len(N)
K = int(K)

answer = -1
visited = [[False]*1000001 for i in range(K+1)]
def dfs(idx) :
  global answer
  if idx == K :
    answer = max(answer, int(''.join(N)))
    return
  for i in range(M-1) :
    for j in range(i+1, M) :
      if i == 0 and N[j] == '0' :
        continue
      N[i], N[j] = N[j], N[i]
      num = int(''.join(N))
      if not visited[idx][num] :
        visited[idx][num] = True
        dfs(idx + 1)
      N[i], N[j] = N[j], N[i]

dfs(0)
print(answer)