from collections import deque
MAX = float('inf')
di = [0, 1, 1]
dj = [-1, 0, -1]


string = list(input().strip())

def cal_dp(target) :
  result = MAX
  dp = [[MAX]*len(string) for _ in range(len(string))]
  dp[0][-1] = 0
  q = deque([(0, len(string)-1, 0)])

  while q :
    i, j, dist = q.popleft()
    if i >= j :
      result = min(result, dist)
      continue
    if target[i] == target[j] :
      if dp[i+1][j-1] > dist :
        dp[i+1][j-1] = dist
        q.append((i+1, j-1, dist))
      continue
    for k in range(3) :
      ai, aj = i + di[k], j + dj[k]
      if dp[ai][aj] > dist + 1 :
        dp[ai][aj] = dist + 1
        q.append((ai, aj, dist+1))

  return result

answer = cal_dp(string)
for i in range(len(string)-1) :
  for j in range(i+1, len(string)) :
    if string[i] == string[j] :
      continue
    string[i], string[j] = string[j], string[i]
    answer = min(answer, cal_dp(string)+1)
    string[i], string[j] = string[j], string[i]

print(answer)