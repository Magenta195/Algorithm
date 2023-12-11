from functools import cmp_to_key
import sys
input = sys.stdin.readline

def largest_sort(x, y) :
  if x+y > y+x :
    return -1
  else :
    return 1

def biggest_sort(x, y) :
  if int(x + x) > int(y + y) :
    return -1
  else :
    return 1

K, N = map(int, input().split())
M = N-K
nums = [input().strip() for _ in range(K)]
nums.sort(key = cmp_to_key(largest_sort))
best_val = sorted(nums, key = cmp_to_key(biggest_sort))[0]

ans = ''
for n in nums :
  if n == best_val :
    ans += n*(M+1)
    best_val = ''
  else :
    ans += n
print(ans)