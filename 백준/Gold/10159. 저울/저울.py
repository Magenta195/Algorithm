import sys
input = sys.stdin.readline
MAX = float('inf')
N = int(input())
M = int(input())
map_list = [[MAX]*N for _ in range(N)]
cvt = lambda x : int(x) - 1

for _ in range(M) :
  a, b = map(cvt, input().split())
  map_list[a][b] = 1

for k in range(N) :
  for i in range(N) :
    for j in range(N) :
      if map_list[i][j] > map_list[i][k] + map_list[k][j] :
        map_list[i][j] = map_list[i][k] + map_list[k][j]

result = [0]*N

for i in range(N-1) :
  for j in range(i+1, N) :
    if map_list[i][j] == map_list[j][i] == MAX :
      result[i] += 1
      result[j] += 1
for i in range(N) :
  print(result[i])