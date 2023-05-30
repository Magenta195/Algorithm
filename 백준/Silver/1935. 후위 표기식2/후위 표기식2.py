N = int(input())
cal_list = input().strip()
cal_dict = dict()
stk = list()
for i in range(N) :
  cal_dict[chr(ord('A') + i)] = int(input())

for c in cal_list :
  if c in ['+', '-', '/', '*'] :
    b = stk.pop()
    a = stk.pop()
    if c == '+' :
      a += b
    elif c == '-' :
      a -= b
    elif c == '/' :
      a /= b
    else :
      a *= b
    stk.append(a)
  else :
    stk.append(cal_dict[c])

print('{:.02f}'.format(stk[0]))