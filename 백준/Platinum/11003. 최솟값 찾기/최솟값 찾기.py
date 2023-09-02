from collections import deque
N, L = map(int, input().split())
num_list = list(map(int, input().split()))
dq = deque()
D_list = list()
for i in range(N) :
  while dq and dq[-1][0] > num_list[i] :
    dq.pop()
  while dq and dq[0][1] < i - L + 1 :
    dq.popleft()
  dq.append((num_list[i], i))
  D_list.append(dq[0][0])
print(*D_list)