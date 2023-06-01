import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]

def divide_and_conquer(start, end) :
  if start == end :
    return num_list[start]
  mid = (start + end) // 2
  left_val = divide_and_conquer(start, mid)
  right_val = divide_and_conquer(mid+1, end)

  h = min(num_list[mid:mid+2])
  mid_val = h*2
  l, r = mid, mid+1
  while start < l or r < end :
    if r == end :
      l -= 1
      h = min(h, num_list[l])
    elif l == start :
      r += 1
      h = min(h, num_list[r])
    elif num_list[l-1] < num_list[r+1] :
      r += 1
      h = min(h, num_list[r])
    else :
      l -= 1
      h = min(h, num_list[l])
    mid_val = max(mid_val, h*(r-l+1))

  return max(left_val, right_val, mid_val)

print(divide_and_conquer(0, len(num_list)-1))