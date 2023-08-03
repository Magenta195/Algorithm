import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]
stk = [ num_list[0] ]

def binary_search(num) :
  start, end = 0, len(stk)-1
  while start < end :
    mid = (start + end) // 2
    if stk[mid] >= num :
      end = mid
    else :
      start = mid + 1
  return end

for num in num_list[1:] :
  if num >= stk[-1] :
    stk.append(num)
  else :
    idx = binary_search(num)
    stk[idx] = num

print(N - len(stk))