from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
prob_list = [list(map(int, input().split())) for _ in range(N)]
prob_list.sort(key = lambda x : (x[0], -x[-1]))

result = list()
for deadline, reward in prob_list :
  if len(result) >= deadline :
    minval = heappop(result)
    reward = max(minval, reward)
  heappush(result, reward)
print(sum(result))