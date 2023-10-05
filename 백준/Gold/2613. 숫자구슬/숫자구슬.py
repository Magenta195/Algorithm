MAX = float('inf')
N, M = map(int, input().split())
marble_list = list(map(int, input().split()))
sum_marble_list, sum_val = [0], 0
for m in marble_list :
  sum_val += m
  sum_marble_list.append(sum_val)

dp = [[(MAX, -1)]*(M+1) for _ in range(N+1)]
dp[0][0] = (0, 0)

for i in range(1, M+1) :
  for j in range(1, N+1) :
    for k in range(j) :
      if dp[k][i-1][0] == MAX :
        continue
      maxval = max(dp[k][i-1][0], sum_marble_list[j] - sum_marble_list[k])
      if maxval < dp[j][i][0] :
        dp[j][i] = (maxval, k)


answer, prev, idx = [0]*M, N, M
while idx :
  _, _prev = dp[prev][idx]
  answer[idx-1] = prev - _prev
  prev = _prev
  idx -= 1
print(dp[-1][-1][0])
print(*answer)