N, F, S = map(int, input().split())
F -= 1
S -= 1
cnt = 0
while F != S :
  F //= 2
  S //= 2
  cnt += 1
print(cnt)