N = int(input())
num_list = list(map(int, input().split()))
ans = -float('inf')
nums = [0]*N
depth_list = [0]*N

def div_and_con(start, end, depth, idx) :
  mid = (start + end) // 2
  depth_list[mid] = depth
  nums[mid] = num_list[idx-1]
  if start == end :
    return 
  div_and_con(start, mid-1, depth+1, idx*2)
  div_and_con(mid+1, end, depth+1, idx*2+1)

def maximum_subquery(mindepth, maxdepth) :
  global ans
  tmp = None
  result = -float('inf')
  for i in range(N) :
    if not mindepth <= depth_list[i] <= maxdepth :
      continue
    if tmp is None :
      tmp = nums[i]
    else :
      tmp = max(tmp + nums[i], nums[i])
    result = max(result, tmp)
  ans = max(ans, result)

div_and_con(0, N-1, 0, 1)
maxdepth = max(depth_list)
for i in range(maxdepth+1) :
  for j in range(i, maxdepth+1) :
    maximum_subquery(i, j)
print(ans)