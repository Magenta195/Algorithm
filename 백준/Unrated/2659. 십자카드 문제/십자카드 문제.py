clock_num_dict = dict()
_range = range(1, 10)

def rotate(s) :
  return s[1:] + s[0]

def clock_num_search(s) :
  clock_num = s
  num_list = list()
  num_list.append(s)
  
  for _ in range(3) :
    _s = rotate(s)
    if s > _s :
      clock_num = _s
    s = _s
    num_list.append(s)
  for num in num_list :
    clock_num_dict[num] = clock_num

  return clock_num

def init() :
  clock_num = ''.join(input().split())
  clock_num = clock_num_search(clock_num)
  return clock_num

def full_search(clock_num) :
  cnt = 1
  for i in _range :
    for j in _range :
      for k in _range :
        for l in _range :
          s = ''.join(map(str, [i, j, k, l]))
          if s in clock_num_dict :
            if clock_num_dict[s] == clock_num :
              return cnt
            continue
          clock_num_search(s)
          cnt += 1

  return -1

def solve() :
  clock_num = init()
  result = full_search(clock_num)
  print(result)

solve()