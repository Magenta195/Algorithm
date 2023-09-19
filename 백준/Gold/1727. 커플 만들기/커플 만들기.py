import sys
input = sys.stdin.readline
MAX = float('inf')

n, m = map(int, input().split())
man_list = list(map(int, input().split()))
woman_list = list(map(int, input().split()))
man_list.sort()
woman_list.sort()
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1) :
  for j in range(1, m+1) :
    if i == j :
      dp[i][j] = dp[i-1][j-1] + abs(man_list[i-1] - woman_list[j-1])
    elif i < j :
      dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(man_list[i-1] - woman_list[j-1]))
    else :
      dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + abs(man_list[i-1] - woman_list[j-1]))
        
print(dp[-1][-1])