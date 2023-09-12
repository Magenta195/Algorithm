from collections import deque

N, M = map(int, input().split())
light_list = list(map(int, input().split()))
light_q = deque()
answer = list()

for i in range(2*M-1) :
  while light_q and light_q[-1][1] < light_list[i] :
    light_q.pop()
  light_q.append((i, light_list[i]))
answer.append((light_q[0][1]))

for i in range(2*M-1, N) :
  while light_q and light_q[-1][1] < light_list[i] :
    light_q.pop()
  while light_q and light_q[0][0] <= i - 2*M + 1 :
    light_q.popleft()
  light_q.append((i, light_list[i]))
  answer.append((light_q[0][1]))

print(*answer)