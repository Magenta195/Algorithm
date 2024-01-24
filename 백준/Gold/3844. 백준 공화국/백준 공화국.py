import sys
input = sys.stdin.readline
MOD = 1000000007
MAX = 10000000

def erastothenes(bound) :
  nums = [True]*(bound+1)
  for i in range(2, bound+1) :
    if nums[i] :
      for j in range(i+i, bound+1, i) :
        nums[j] = False
  return nums

def pow(n, k) :
  if k == 0 :
    return 1
  if k == 1 :
    return n
  p = pow(n, k // 2)
  p = (p * p) % MOD
  if k % 2 :
    p = (p * n) % MOD
  return p

def solve() :
  n = int(input())
  if n == 0 :
    return False
  result = 1
  for i in range(2, n//2+1) :
    if not nums[i] :
      continue
    cnt = 0
    j = i
    while j <= n :
      cnt += n // j
      j *= i
    if cnt % 2 :
      cnt -= 1
    result = (result * pow(i, cnt)) % MOD
  print(result)
  return True

nums = erastothenes(MAX//2)
while solve() :
  continue