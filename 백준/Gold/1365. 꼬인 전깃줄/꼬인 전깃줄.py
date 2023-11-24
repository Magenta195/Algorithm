
N = int(input())
nums = list(map(int, input().split()))
n_list = list()

def upper_bound(val) :
  start, end = 0, len(n_list)-1
  while start < end :
    mid = (start + end) // 2
    if n_list[mid] < val :
      start = mid+1
    else :
      end = mid
  return end

for num in nums :
  if not n_list or n_list[-1] < num :
    n_list.append(num)
  else :
    idx = upper_bound(num)
    n_list[idx] = num

print(N-len(n_list))
    