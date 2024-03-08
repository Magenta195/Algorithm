N = 100
dp = [[0]*3 for _ in range(N+1)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 1]
dp[3] = [1, 0, 1]

for i in range(4, N+1) :
  for j in range(3) :
    dp[i][j] += dp[i-2][j] + dp[i-3][j]

ptype = int(input())
num = int(input())

if ptype == 1 :
  print(sum(dp[num]))
elif ptype == 2 :
  idx = int(input())
  while num >= 4 :
    if sum(dp[num-3]) >= idx :
      num -= 3
    else :
      idx -= sum(dp[num-3])
      num -= 2
  if num == idx == 1 or num == 3 and idx == 2 :
    print('X')
  elif num == 2 and idx == 1 :
    print('Y')
  else :
    print('Z')
else :
  idx = ord(input()) - ord('X')
  print(dp[num][idx])