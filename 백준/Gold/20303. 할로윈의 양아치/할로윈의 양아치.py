from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

candy_list = list(map(int, input().split()))
friend_dict = defaultdict(list)
visited = [False]*N
total_candy = list()

for _ in range(M) :
  a, b = map(int, input().split())
  friend_dict[a-1].append(b-1)
  friend_dict[b-1].append(a-1)

for i in range(N) :
  if not visited[i] :
    people, candy = 1, candy_list[i]
    visited[i] = True
    q = deque([i])

    while q :
      now = q.popleft()
      for nxt in friend_dict[now] :
        if not visited[nxt] :
          visited[nxt] = True
          people += 1
          candy += candy_list[nxt]
          q.append(nxt)
    
    total_candy.append((people, candy))

dp = [[-1]*K for _ in range(len(total_candy)+1)]
dp[0][0] = 0

for i in range(len(total_candy)) :
  dp[i][0] = 0
  people, candy = total_candy[i]
  for j in range(K) :
    if dp[i][j] > -1 :
      dp[i+1][j] = max(dp[i+1][j], dp[i][j])
      if j + people < K :
        dp[i+1][j+people] = max(dp[i+1][j+people], dp[i][j] + candy)

print(max(dp[-1]))