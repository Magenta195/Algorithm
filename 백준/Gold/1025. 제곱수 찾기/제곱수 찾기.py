import sys
input = sys.stdin.readline

ans = -1
N, M = map(int, input().split())
maps = [input().strip() for _ in range(N)]

for i in range(N) :
  for j in range(M) :
    for k in range(-N, N) :
      for l in range(-M, M) :
        if not k and not l :
          continue
        _i, _j, tmp = i, j, ''
        while -1 < _i < N and -1 < _j < M :
          tmp += maps[_i][_j]
          if int(int(tmp) ** 0.5) ** 2 == int(tmp) :
            ans = max(ans, int(tmp))
          _i += k
          _j += l
print(ans)