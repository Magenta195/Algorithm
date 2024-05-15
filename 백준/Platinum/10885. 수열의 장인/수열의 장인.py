import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

MOD = 1000000007


def pow_two(n):
  if n == 0 :
    return 1
  if n == 1:
    return 2
  p = pow_two(n // 2) % MOD
  p = p * p % MOD
  if n % 2 == 1:
    return p * 2 % MOD
  return p


def solve():
  N = int(input())
  numbers = list(map(int, input().split()))
  dp = [[-1] * N for _ in range(2)]
  adder = 1 if abs(numbers[0]) == 2 else 0
  if numbers[0] > 0:
    dp[0][0] = adder
  elif numbers[0] < 0:
    dp[1][0] = adder

  for i in range(1, N):
    if numbers[i] == 0:
      continue
    adder = 1 if abs(numbers[i]) == 2 else 0

    if numbers[i] > 0:
      dp[0][i] = max(dp[0][i - 1] + adder, adder)
      if dp[1][i-1] > -1 :
        dp[1][i] = dp[1][i - 1] + adder
    else:
      if dp[1][i-1] > -1 :
        dp[0][i] = dp[1][i - 1] + adder
      dp[1][i] = max(dp[0][i - 1] + adder, adder)

  pos_result = max(dp[0])
  full_result = max(numbers)
  if pos_result == -1:
    print(full_result)
  else:
    print(pow_two(pos_result))


if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    solve()
