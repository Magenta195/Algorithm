DNA = input().strip()
l = len(DNA)
dp = [[0]*l for _ in range(l)]

for i in range(1, l) :
  for j in range(l-i) :
    if (DNA[j] == 'a' and DNA[j+i] == 't') or (DNA[j] == 'g' and DNA[j+i] == 'c') :
      dp[j][j+i] = dp[j+1][j+i-1] + 2
    for k in range(j, j+i) :
      if dp[j][j+i] < dp[j][k] + dp[k+1][j+i] :
        dp[j][j+i] = dp[j][k] + dp[k+1][j+i]

print(dp[0][-1])