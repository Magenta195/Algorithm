day_list = [
  "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ]
day_dict = { i : day_list[i] for i in range(7) }
MAX = 500000

def time_convert(s) :
  h, m = map(int, s.split(':'))
  return h*60 + m

def rev_time_convert(num) :
  d, h, m = num // 1440, (num % 1440) // 60, (num % 1440) % 60
  return d % 7, '{:02d}:{:02d}'.format(h, m)

def init() :
  a_start = time_convert(input().strip())
  b_start = time_convert(input().strip())
  a_margin = time_convert(input().strip())
  b_margin = time_convert(input().strip())

  return a_start, a_margin, b_start, b_margin

def traversal(a_start, a_margin, b_start, b_margin) :
  for i in range(MAX) :
    t = a_start + a_margin * i
    if t - b_start >= 0 and not (t - b_start) % b_margin :
      return t

  return -1

def solve() :
  a_start, a_margin, b_start, b_margin = init()
  visited = [0]*25200

  result = traversal(a_start, a_margin, b_start, b_margin)

  if result == -1 :
    print('Never')
  else :
    day, t = rev_time_convert(result)
    print(day_dict[day])
    print(t)

solve()