N, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list.sort()
b_list.sort()

lst = [1, 2, 3, 3, 4, 5]

def mul_binary_search(mul, val) :
  start, end = 0, N
  while start < end :
    mid = (start + end) // 2
    num = b_list[mid] * mul
    if num > val :
      end = mid
    else :
      start = mid + 1
  return end

def full_binary_search() :
  start, end = a_list[0]*b_list[0], a_list[-1]*b_list[-1]
  while start < end :
    mid = (start + end) // 2
    cnt = 0
    for a in a_list :
      cnt += mul_binary_search(a, mid)
    if cnt >= K :
      end = mid
    else :
      start = mid + 1
  return end

print(full_binary_search())