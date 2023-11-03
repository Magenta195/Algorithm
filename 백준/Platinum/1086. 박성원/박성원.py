from math import factorial
N = int(input())
lst = [input().strip() for _ in range(N)]
K = int(input())
modlen_lst = [(10**len(x))%K for x in lst]
rest_lst = [int(x)%K for x in lst]
dp = [[-1]*(1<<N) for _ in range(K)]

def dfs(visited, rest):
  if visited == (1<<N) - 1:
    return 1 if rest == 0 else 0
  if dp[rest][visited] > -1 :
    return dp[rest][visited]
  dp[rest][visited] = 0
  for i in range(N):
    if (1<<i) | visited == visited : continue
    n_rest = ((rest*modlen_lst[i])%K + rest_lst[i])%K
    dp[rest][visited] += dfs((1<<i)|visited, n_rest)
  return dp[rest][visited]

def gcd(a, b):
  while b > 0 :
    a %= b
    a,b = b, a
  return a
dfs(0,0)

a, b = dp[0][0], factorial(N)
if a == 0 :
  print('0/1')
else : 
  r = gcd(a,b)
  print('{}/{}'.format(a//r,b//r))