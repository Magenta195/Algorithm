N = int(input())
cur_list = list(map(int, input().split()))
target_list = list(map(int, input().split()))
diff_list = [ target_list[i] - cur_list[i] for i in range(N) ]
dp = [0]*N
dp[0] = abs(diff_list[0])

for i in range(1, N) :
  if diff_list[i] * diff_list[i-1] > 0 :
    dp[i] = dp[i-1] + max(0, abs(diff_list[i]) - abs(diff_list[i-1]))
  else :
    dp[i] = dp[i-1] + abs(diff_list[i])

print(dp[-1])