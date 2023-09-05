import sys
MAX = float('inf')
input = sys.stdin.readline

N, M = map(int, input().split())
P_list = [list(map(int, input().split())) for _ in range(N)]
answer = MAX
p_col = [0]*M

def dfs(n_idx, m_num) :
  if n_idx == N :
    for i in range(M) :
      if p_col[i] <= 0 :
        return MAX
    return 0
  p_row = [0]*M
  for i in range(M-1, -1, -1) :
    p_row[i] = -P_list[n_idx][i] if m_num & (1 << i) else P_list[n_idx][i]

  sum_row = sum(p_row)
  if sum_row == 0 :
    return MAX
  for i in range(M) :
    p_col[i] += p_row[i] if sum_row > 0 else -p_row[i]
  result = dfs(n_idx+1, m_num)
  if sum_row < 0 :
    result += 1
  for i in range(M) :
    p_col[i] -= p_row[i] if sum_row > 0 else -p_row[i]
  return result

for i in range(1 << M) :
  answer = min(answer, dfs(0, i) + bin(i)[2:].count('1'))
print(answer if answer < MAX else -1)