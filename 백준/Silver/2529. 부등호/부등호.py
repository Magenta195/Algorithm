
visited = [-1]*10
result = list()

def init() :
  global N
  N = int(input())
  ineq_list = list(input().split())
  return ineq_list

def make_num() :
  result = [0]*(N+1)
  for i in range(10) :
    if visited[i] > -1 :
      result[visited[i]] = str(i)

  return ''.join(result)

def dfs(prev_num, ineq_list, idx) :
  if idx == N+1 :
    result.append(make_num())
    return

  if ineq_list[idx-1] == '>' :
    _range = range(prev_num-1, -1, -1)
  else :
    _range = range(prev_num+1, 10)

  for i in _range :
    if visited[i] == -1 :
      visited[i] = idx
      dfs(i, ineq_list, idx+1)
      visited[i] = -1

def result_out() :
  result.sort()
  print(result[-1])
  print(result[0])

def solve() :
  ineq_list = init()
  for i in range(10) :
    visited[i] = 0
    dfs(i, ineq_list, 1)
    visited[i] = -1
  result_out()

solve()