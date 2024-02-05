from collections import defaultdict
import sys
input = sys.stdin.readline

def gcd(a, b) :
  while b :
    a, b = b, a%b
  return a

def solve() :
  N = int(input())
  nums = list(map(int, input().split()))
  stk = defaultdict(lambda : N)
  ans = 0
  for i in range(N) :
    next_stk = defaultdict(lambda : N)
    for key, val in stk.items() :
      g = gcd(nums[i], key)
      next_stk[g] = min(next_stk[g], val)
      ans = max(ans, g * (i-next_stk[g]+1))
    next_stk[nums[i]] = min(next_stk[nums[i]], i)
    stk = next_stk
    ans = max(ans, nums[i])
  print(ans)

for _ in range(int(input())) :
  solve()