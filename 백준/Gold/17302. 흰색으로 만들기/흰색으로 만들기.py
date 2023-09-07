import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
map_list = [list(input().strip()) for _ in range(N)]
answer = [['2']*M for _ in range(N)]

def reverse(x, y) :
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < M and -1 < ay < N :
      map_list[ay][ax] = 'B' if map_list[ay][ax] == 'W' else 'W'

for i in range(N) :
  for j in range(M) :
    reverse(j, i)

for i in range(N) :
  for j in range(M) :
    if map_list[i][j] == 'B' :
      answer[i][j] = '3'

print(1)
for _answer in answer :
  print(''.join(_answer))