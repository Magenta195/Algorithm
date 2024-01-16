N, T = map(int, input().split())
nums = list(map(int, input().split()))
if N == 1 :
  exit()
if N == 2 :
  print(1)
  exit()

t = T - nums[0] + nums[1]
s = sum(nums[2:])
target = (t + s) // 2
is_pos = [False]*N
dp = [[list() for _ in range(target+1)] for _ in range(N)]

for i in range(2, N) :
  if nums[i] > target :
    continue
  dp[i][nums[i]].append(i)
  
for i in range(2, N-1) :
  for j in range(target+1) :
    if not dp[i][j] :
      continue
    if not dp[i+1][j] :
      dp[i+1][j] += dp[i][j]
    if j + nums[i+1] <= target and not dp[i+1][j+nums[i+1]] :
      dp[i+1][j+nums[i+1]] += dp[i][j]
      dp[i+1][j+nums[i+1]].append(i+1)

for i in dp[-1][target] :
  is_pos[i] = True

cnt = 0 
for i in range(2, N) :
  if not is_pos[i] :
    while cnt :
      cnt -= 1
      print(2)
    print(1)
  else :
    cnt += 1
while cnt :
  cnt -= 1
  print(2)
print(1)