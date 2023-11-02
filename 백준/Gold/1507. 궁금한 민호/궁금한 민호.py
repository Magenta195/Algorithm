import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
direct = [[True]*N for _ in range(N)]
for k in range(N) :
  for i in range(N) :
    for j in range(N) :
      if i == j or i == k or k == j :
        continue
      if maps[i][j] > maps[i][k] + maps[k][j] :
        print(-1)
        exit()
      elif maps[i][j] == maps[i][k] + maps[k][j] :
        direct[i][j] = direct[j][i] = False

maps = [[ maps[i][j] if direct[i][j] else 0 for j in range(N)] for i in range(N)]
print(sum(map(sum, maps)) // 2)

