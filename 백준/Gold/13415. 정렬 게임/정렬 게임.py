from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
K = int(input())
stk = []
for i in range(K) :
  a, b = map(int, input().split())
  for j, k in [(a-1, 1), (b-1, -1)] :
    while stk and stk[-1][0] <= j :
      stk.pop()
    stk.append((j, k))

stk.append((-1, 0))
sorted_nums = deque(sorted(nums[:stk[0][0]+1]))
for i in range(len(stk)-1) :
  cur, cur_d = stk[i]
  nxt, _ = stk[i+1]
  for j in range(cur, nxt, -1) :
    n = sorted_nums.pop() if cur_d == 1 else sorted_nums.popleft()
    nums[j] = n

print(*nums)