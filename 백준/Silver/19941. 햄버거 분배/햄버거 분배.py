N, K = map(int, input().split())
visited = [False]*N
map_list = input().strip()
answer = 0
for i in range(N) :
  if map_list[i] == 'H' :
    continue
  for j in range(i-K, i+K+1) :
    if not -1 < j < N :
      continue
    if map_list[j] == 'H' and not visited[j] :
      visited[j] = True
      answer += 1
      break
print(answer)