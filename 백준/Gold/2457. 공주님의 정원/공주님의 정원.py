import sys
input = sys.stdin.readline
month_list = [31, 30, 31, 30, 31, 31, 30, 31]

def cal_days(month, days) :
  if month < 0 :
    return 0
  if month > 8 :
    return 276
  if month == 0 :
    return days
  return cal_days(month-1, days+month_list[month-1])

day_list = list() # cal_days 11.30 : 275

N = int(input())
for _ in range(N) :
  sm, sd, em, ed = map(int, input().split())
  sd = max(1, cal_days(sm-3, sd))
  ed = min(275, cal_days(em-3, ed)-1)
  if sd == 276 or ed == 0 or sd > ed :
    continue
  day_list.append((sd, ed))

day_list.sort(key = lambda x : (x[0], -x[1]))
flower_list = list()
for sd, ed in day_list :
  if not flower_list :
    flower_list.append((sd, ed))
  elif flower_list[-1][0] <= sd and ed <= flower_list[-1][1] :
    continue
  elif len(flower_list) > 1 and ( sd <= flower_list[-2][1] or flower_list[-2][1] + 1 == sd ) :
    if ed > flower_list[-1][1] :
      flower_list[-1] = (sd, ed)
  elif flower_list[-1][1] >= sd or flower_list[-1][1] + 1 == sd:
    flower_list.append((sd, ed))
  else :
    break
if not flower_list or flower_list[0][0] != 1 or flower_list[-1][1] < 275 :
  print(0)
else :
  print(len(flower_list))