import sys
input = sys.stdin.readline

N = int(input())
balls = input().strip()
ball_cnt = {'R' : 0, 'B' : 0}

for ball in balls :
  ball_cnt[ball] += 1

ans = float('inf')
for b in ['R', 'B'] :
  flg = True
  for _balls in [balls, balls[::-1]] :
    if _balls[0] != b :
      continue
    cnt = 1
    flg = False
    for _b in _balls[1:] :
      if _b != b :
        break
      cnt += 1
    ans = min(ans, ball_cnt[b] - cnt)

  if flg :
    ans = min(ans, ball_cnt[b])

print(ans)