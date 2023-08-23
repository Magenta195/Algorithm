from collections import deque
MAX = 500001

N, K = map(int, input().split())
answer_list = [K]
t = 1
while answer_list[-1] < MAX :
  answer_list.append(answer_list[-1] + t)
  t += 1

q = deque([(N, 0)])
visited = [[MAX]*MAX for _ in range(2)]
visited[0][N] = 0
answer = MAX
while q :
  now, t = q.popleft()
  for nxt in [now*2, now-1, now+1] :
    if -1 < nxt < MAX and visited[(t+1)%2][nxt] > t+1 and answer_list[t+1] < MAX :
      visited[(t+1)%2][nxt] = t + 1
      q.append((nxt, t+1))

for t, now in enumerate(answer_list[:-1]) :
  if visited[t%2][now] <= t :
    answer = min(answer, t)
print(answer if answer < MAX else -1)