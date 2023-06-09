import sys

N = int(input())
result_list = list(map(int, input().split()))
result_list.reverse()

answer_list = [0]*N

def is_inside_zeros(start, end) :
  if start < end :
    return 0 in answer_list[start:end]
  else :
    return 0 in answer_list[:end] and 0 in answer_list[start:]

def dfs(frm, idx) :
  answer_list[frm] = result_list[idx]
  if idx == N-1 :
    for _ in range(frm) :
      answer_list.append(answer_list.pop(0))
    print(N)
    print(*answer_list)
    return True

  is_enable = False
  _frm = frm
  while True :
    prev_frm = ( _frm - result_list[idx+1] ) % N
    if not answer_list[prev_frm]:
      is_enable |= dfs(prev_frm, idx+1)
    _frm = (_frm - 1) % N
    if answer_list[_frm] or _frm == frm :
      break

  answer_list[frm] = 0
  return is_enable


flg = dfs(0, 0)
if not flg :
  print(-1)