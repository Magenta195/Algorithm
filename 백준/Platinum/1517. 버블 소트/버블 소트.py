N = int(input())
num_list = list(map(int, input().split()))

def div_and_conquer(start, end) :
  if start == end :
    return 0

  mid = (start + end) // 2
  lval = div_and_conquer(start, mid)
  rval = div_and_conquer(mid+1, end)
  
  val, lst = lval + rval, list()
  l, r = start, mid+1 
  while l <= mid and r <= end :
    if num_list[l] <= num_list[r] :
      lst.append(num_list[l])
      l += 1
    else :
      lst.append(num_list[r])
      r += 1
      val += mid - l + 1

  if l <= mid :
    for i in range(l, mid+1) :
      lst.append(num_list[i])
  if r <= end :
    for i in range(r, end+1) :
      lst.append(num_list[i])

  for i in range(start, end+1) :
    num_list[i] = lst[i-start]

  return val

print(div_and_conquer(0, N-1))
