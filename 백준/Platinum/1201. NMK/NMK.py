import math
N, M, K = map(int, input().split())

if M + K > N + 1 or M*K < N:
  print(-1)
  exit()
if M == 1 :
  print(*range(N, 0, -1))
  exit()
if K == 1 :
  print(*range(1, N+1))
  exit()

ans = list(range(K, 0, -1))
cur = K + 1
dec_len, left_dec = (N-K) // (M-1), (N-K) % (M-1)

while cur <= N :
  nxt = cur + dec_len - 1
  if left_dec :
    nxt += min(left_dec, K - dec_len)
    left_dec -= min(left_dec, K - dec_len)
  ans += list(range(nxt, cur-1, -1))
  cur = nxt+1
print(*ans)