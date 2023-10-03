from collections import deque
import math
import sys
input = sys.stdin.readline
MAX = float('inf')

N, K = map(int, input().split())
airport_list = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)] + [(10000, 10000)]

airport_fuel_list = [[0]*(N+2) for _ in range(N+2)]

for i in range(N+1) :
  ix, iy = airport_list[i]
  for j in range(i+1, N+2) :
    jx, jy = airport_list[j]
    fuel = math.ceil(((ix - jx) ** 2 + (iy - jy) ** 2 ) ** 0.5 / 10)
    airport_fuel_list[i][j] = airport_fuel_list[j][i] = fuel

def bfs(value) :
  visited = [-1]*(N+2)
  visited[0] = K
  q = deque([(0, K)])
  while q :
    node, left_landing = q.pop()
    if node == N+1 :
      return True
    if not left_landing :
      if airport_fuel_list[node][-1] <= value :
        return True
      continue
    for i in range(N+2) :
      if i != node and airport_fuel_list[node][i] <= value and left_landing and visited[i] < left_landing-1 :
        visited[i] = left_landing-1
        q.append((i, left_landing-1))
  return False

start, end = 0, 1416
while start < end :
  mid = (start + end) // 2
  if bfs(mid) :
    end = mid
  else :
    start = mid + 1
print(end)