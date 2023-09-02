from heapq import heappush, heappop

N, L = map(int, input().split())
num_list = list(map(int, input().split()))
dq = list()
D_list = list()

for i in range(N) :
  while dq and dq[0][1] < i - L + 1:
    heappop(dq)
  heappush(dq, (num_list[i], i))
  D_list.append(dq[0][0])
print(*D_list)