import sys
input = sys.stdin.readline

n = int(input())
ipt = list(map(int, input().split()))
opt = [0]*n
for i in range(n) :
  opt[ipt[i]-1] = i

stk = list()

def lower_bound(target) :
  start, end = 0, len(stk)
  while start < end :
    mid = (start + end) // 2
    if stk[mid] < target :
      start = mid + 1
    else :
      end = mid
  return end

for o in opt :
  idx = lower_bound(o)
  if idx == len(stk) :
    stk.append(o)
  else :
    stk[idx] = o
print(len(stk))