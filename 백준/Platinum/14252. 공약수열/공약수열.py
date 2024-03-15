MAX = 10**6+1
N = int(input())
nums = sorted(map(int, input().split()))

def gcd(a, b) :
  while b :
    a, b = b, a % b
  return a

def search(a, b) :
  if gcd(a, b) == 1 :
    return 0

  left_list = []
  right_list = []
  for i in range(a+1, b) :
    cnt = 0
    if gcd(a, i) == 1 :
      left_list.append(i)
      cnt += 1
    if gcd(b, i) == 1 :
      right_list.append(i)
      cnt += 1
    if cnt == 2 :
      return 1

  res = MAX
  for i in right_list :
    for j in left_list :
      if i < j :
        break
      if gcd(i, j) == 1 :
        return 2
      res = min(res, search(j, i)+2)  
  return res

ans = 0
for i in range(N-1) :
  ans += search(nums[i], nums[i+1])

print(ans)