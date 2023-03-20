N = int(input())
M = int(input())
movable_list = list()

def init() :
  if M == 0 :
    movable_list.append(N)
    return
  prev = 1
  for _ in range(M) :
    now = int(input())
    if now - prev :
      movable_list.append(now - prev)
    prev = now + 1
  if now != N :
    movable_list.append(N - prev + 1)

def make_dp() :
  if not movable_list :
    return list()
    
  max_val = max(movable_list)

  dp = [0]*(max_val+1)
  dp[0] = dp[1] = 1

  for i in range(2, max_val+1) :
    dp[i] = dp[i-1] + dp[i-2]

  return dp

def calculate(dp) :
  result = 1
  for mv in movable_list :
    result *= dp[mv]
  return result

def solve() :
  init()
  dp = make_dp()
  result = calculate(dp)
  print(result)

solve()
