import sys
input = sys.stdin.readline

def cal_length(num) :
  _num, length = 1, 1
  res = 0
  while True :
    if _num * 10 > num :
      res += (num - _num + 1) * length
      break
    res += _num * 9 * length
    _num *= 10
    length += 1
  return res + num - num // 4

def solve() :
  K = int(input())
  if not K :
    return False
  start, end = 0, 10**15
  
  while start < end :
    mid = (start + end) // 2
    if cal_length(mid) >= K :
      end = mid
    else :
      start = mid + 1
  if end % 4 == 0 :
    res = end
  else :
    for i in range(end*10, end*10+10) :
      if i % 4 == 0 :
        res = i
        break
  print(str(res)[K-cal_length(end-1)-1])
  return True

while solve() :
  pass