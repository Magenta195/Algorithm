from collections import deque

bracket_list = [ (i, j) for i in range(5) for j in range(i+1, 6)]

def search(win_list) :
  q = deque([[0, win_list.copy()]])

  while q :
    idx, cur_list = q.popleft()
    if idx == 15 :
      if is_valid_winning(cur_list) :
        return 1
      continue
    
    a, b = bracket_list[idx]

    for k in range(3) :
      if cur_list[3*a+k] and cur_list[3*b+2-k] :
        next_list = cur_list.copy()
        next_list[3*a+k] -= 1
        next_list[3*b+2-k] -= 1
        q.append([idx+1, next_list])

  return 0

def is_valid_winning(lst) :
  for left in lst :
    if left != 0 :
      return False
  return True

def solve() :
  result = list()
  for _ in range(4) :
    win_list = list(map(int, input().split()))
    result.append(search(win_list))

  print(*result)

solve()