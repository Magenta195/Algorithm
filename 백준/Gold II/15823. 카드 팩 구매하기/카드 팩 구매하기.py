from collections import deque

N, M = map(int, input().split())
cards = list(map(int, input().split()))

q = deque()
visited = set()
max_len = [0]*N
for i, c in enumerate(cards) :
  q.append((c, i))
  if c not in visited :
    visited.add(c)
    continue
  while q :
    _c, j = q.popleft()
    max_len[j] = i - j
    if _c == c :
      break
    visited.discard(_c)
while q :
  _c, j = q.popleft()
  max_len[j] = N - j

def calculate(length) :
  dp = [0]*(N+1)
  for i in range(N) :
    if max_len[i] >= length :
      dp[i+length] = max(dp[i+length], dp[i] + 1)
    dp[i+1] = max(dp[i], dp[i+1])
  return dp[-1] >= M

def bisect() :
  start, end = 1, N // M + 1
  ret = 0
  while start < end :
    mid = (start + end) // 2
    if calculate(mid) :
      ret = mid
      start = mid + 1
    else :
      end = mid
  print(ret)

bisect()