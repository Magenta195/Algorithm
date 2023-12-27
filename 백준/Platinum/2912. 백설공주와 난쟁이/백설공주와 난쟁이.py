from collections import defaultdict
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
hats = list(map(int, input().split()))
M = int(input())

hat_dict = defaultdict(int)
ans = [0]*M
queries = [[i] + list(map(lambda x : int(x)-1, input().split())) for i in range(M)]
queries.sort(key = lambda x : (x[1] // (N ** 0.5), x[2]))

def check(K) :
  for key, val in hat_dict.items() :
    if val > K / 2 :
      return key
  return 0

l, r = 0, -1
for idx, i, j in queries :
  while r < j :
    r += 1
    hat_dict[hats[r]] += 1
  while r > j :
    hat_dict[hats[r]] -= 1
    if not hat_dict[hats[r]] :
      del hat_dict[hats[r]]
    r -= 1
  while l < i :
    hat_dict[hats[l]] -= 1
    if not hat_dict[hats[l]] :
      del hat_dict[hats[l]]
    l += 1
  while l > i :
    l -= 1
    hat_dict[hats[l]] += 1
  ans[idx] = check(j - i + 1)

for v in ans :
  if not v :
    print("no")
  else :
    print("yes", v)