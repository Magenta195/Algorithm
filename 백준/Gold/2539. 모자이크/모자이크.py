R, C = map(int, input().split())
needed_paper = int(input())
N = int(input())

def init() :
  max_row = 0
  col_list = list()
  for _ in range(N) :
    r, c = map(int, input().split())
    max_row = max(r, max_row)
    col_list.append(c)

  col_list.sort()
  return max_row, col_list

def cal_paper_num(col_list, sz) :
  result = 1
  prev = col_list[0]-1
  if len(col_list) > 1 :
    for c in col_list :
      if prev + sz < c :
        result += 1
        prev = c-1

  return result

def binary_search(start, end, col_list) :
  result = end
  while start <= end :
    mid = (start + end) // 2
    used_paper = cal_paper_num(col_list, mid)
    if used_paper <= needed_paper :
      result = min(result, mid)
      end = mid - 1
    else :
      start = mid + 1

  return result

def solve() :
  max_row, col_list = init()
  start, end = max_row, R
  result = binary_search(start, end, col_list)
  print(result)

solve()