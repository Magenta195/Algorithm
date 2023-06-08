import sys
input = sys.stdin.readline
MAX = float('inf')

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
dp = [MAX]*(k+1)
dp[0] = 0

for coin in coin_list :
  for i in range(k-coin+1) :
    dp[i+coin] = min(dp[i+coin], dp[i] + 1)

print(dp[-1] if dp[-1] < MAX else -1)