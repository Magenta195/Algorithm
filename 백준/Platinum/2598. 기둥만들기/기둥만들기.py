from collections import deque

side_dict = {
  2 : deque([1, 5, 3, 4]),
  3 : deque([0, 4, 2, 5]),
  0 : deque([1, 4, 3, 5]),
  1 : deque([0, 5, 2, 4]),
  5 : deque([0, 3, 2, 1]),
  4 : deque([0, 1, 2, 3])
}

colors = set(['R', 'G', 'B', 'Y'])
cube_list = [input().strip() for _ in range(4)]
column_dict = { key : list() for key in colors }

top_list = list()
side_list = list()

def column_search(idx) :
  if idx == 4 :
    return make_column(0)

  result = 0
  for i in range(6) :
    top_list.append(i)
    side_list.append(side_dict[i].copy())
    
    result += column_search(idx+1)
    
    top_list.pop()
    side_list.pop()

  return result

def make_column(idx) :
  if idx == 4 :
    return is_valid_column()
  if idx == 0 :
    return make_column(idx+1)

  result = 0
  for i in range(4) :
    result += make_column(idx+1)
    side_list[idx].rotate(1)
  return result
  
def is_valid_column() :
  top = top_list[-1]
  top_color = cube_list[-1][top]
  side_result = deque()

  for i in range(4) :
    side_idx_list = [lst[i] for lst in side_list]

    side_color_list = [cube_list[j][side_idx_list[j]] for j in range(4)]
    if set(side_color_list) != colors :
      return 0
    side_result.append(''.join(side_color_list))

  for _ in range(4) :
    if side_result in column_dict[top_color] :
      return 0
    side_result.rotate(1)

  column_dict[top_color].append(side_result)
  return 1

def solve() :
  result = column_search(0)
  print(result)

solve()
  