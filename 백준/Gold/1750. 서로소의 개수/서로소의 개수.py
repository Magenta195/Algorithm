from collections import defaultdict
import sys
input = sys.stdin.readline
MOD = 10000003
def gcd(a, b) :
  while b > 0 :
    a, b = b, a % b
  return a

N = int(input())
num_list = [int(input()) for _ in range(N)]
count_one = lambda x : x.count(1)
dp = [defaultdict(int) for _ in range(N)]
dp[0][num_list[0]] = 1

for i in range(1, N) :
  for j in dp[i-1].keys() :
    val = gcd(num_list[i], j)
    dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
    dp[i][val] = ( dp[i][val] + dp[i-1][j] ) % MOD
  dp[i][num_list[i]] += 1

print(dp[-1][1] % MOD)