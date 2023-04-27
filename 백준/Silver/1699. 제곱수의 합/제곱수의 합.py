N = int(input())

dp = list(range(N+1))
sq_list = list()

num = 1
while num**2 <= N :
  dp[num**2] = 1
  sq_list.append(num**2)
  num += 1

for i in range(1, N) :
  for j in sq_list :
    if i + j > N :
      break
    dp[i+j] = min(dp[i+j], dp[i] + 1)

print(dp[-1])