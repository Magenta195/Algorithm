import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medal_list = [list(map(int, input().split())) for _ in range(N)]
medal_list.sort()

k, kg, ks, kb = medal_list[K-1]
cnt = 1

for idx, g, s, b in medal_list :
  if idx == K :
    continue
  if g > kg or g == kg and s > ks or g == kg and s == ks and b > kb :
    cnt += 1

print(cnt)