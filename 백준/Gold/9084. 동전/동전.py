import sys
input = sys.stdin.readline

for _ in range(int(input())) :
  N = int(input())
  num_list = list(map(int, input().split()))
  M = int(input())
  dp = [0]*(M+1)
  dp[0] = 1
  for num in num_list :
    for i in range(M-num+1) :
      dp[i+num] += dp[i]
  print(dp[-1])