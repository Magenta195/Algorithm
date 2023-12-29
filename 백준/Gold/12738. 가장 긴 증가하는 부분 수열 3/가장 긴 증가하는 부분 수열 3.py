N = int(input())
num_list = list(map(int, input().split()))
stk = list()

def lower_bound(val) :
  start, end = 0, len(stk)
  while start < end :
    mid = (start + end) // 2
    if val > stk[mid] :
      start = mid + 1
    else :
      end = mid
  return end

for n in num_list :
  idx = lower_bound(n)
  if idx == len(stk) :
    stk.append(n)
  else :
    stk[idx] = n
print(len(stk))
