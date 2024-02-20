import sys
input = sys.stdin.readline
N, L = map(int, input().split())
kimchi = [int(input()) for _ in range(N)]
left = sorted([k for k in kimchi if k < L], reverse = True)
right = sorted([k for k in kimchi if k >= L])
MAX = float('inf')
dp = [[[MAX]*2 for _ in range(len(right)+1)] for _ in range(len(left)+1)]
if left :
  dp[1][0][0] = abs(L-left[0])*N
if right :
  dp[0][1][1] = abs(L-right[0])*N

for i in range(1, N) :
  for j in range(i+1) :
    l, r = j, i-j
    for k in range(2) :
      if l > len(left) or r > len(right) or dp[l][r][k] == MAX :
        continue
      if l+1 <= len(left) :
        if k == 0 and l > 0 :
          dist = abs(left[l] - left[l-1])
        elif k == 1 and r > 0 : 
          dist = abs(left[l] - right[r-1])
        else :
          dist = MAX
        dp[l+1][r][0] = min(dp[l+1][r][0], dp[l][r][k] + (N-i)*dist)
      if r+1 <= len(right) :
        if k == 0 and l > 0 :
          dist = abs(right[r] - left[l-1]) 
        elif k == 1 and r > 0 : 
          dist = abs(right[r] - right[r-1])
        else :
          dist = MAX
        dp[l][r+1][1] = min(dp[l][r+1][1], dp[l][r][k] + (N-i)*dist)
print(min(dp[-1][-1]))