from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
basic_parts = list()
topologic_parts = [0]*N
next_parts = [defaultdict(int) for _ in range(N)]
needed_parts = [defaultdict(int) for _ in range(N)]

q = deque()

for _ in range(M) :
  x, y, k = map(int, input().split())
  topologic_parts[x-1] += 1
  next_parts[y-1][x-1] += k

for i in range(N) :
  if topologic_parts[i] == 0 :
    q.append(i)
    basic_parts.append(i)
    needed_parts[i][i] = 1


while q :
  node = q.popleft()

  for nxt, mul in next_parts[node].items() :
    for key, val in needed_parts[node].items() :
      needed_parts[nxt][key] += val*mul
    topologic_parts[nxt] -= 1
    if topologic_parts[nxt] == 0 :
      q.append(nxt)

for key, val in sorted(needed_parts[-1].items()) :
  print(key+1, val)