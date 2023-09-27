from heapq import heappush, heappop

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
nums = ''

for i in range(3) :
  num = input().strip().replace(" ","")
  for j in range(3) :
    if num[j] == '0' :
      x, y = j, i
  nums += num

q = [(0, x, y, nums)]
visited = set([nums])

while q :
  move, x, y, nums = heappop(q)
  if nums == '123456780' :
    print(move)
    exit()
  nums = list(nums)
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < 3 and -1 < ay < 3 :
      nums[x + y*3], nums[ax + ay*3] = nums[ax + ay*3], nums[x + y*3]
      tmp = ''.join(nums)
      if tmp not in visited :
        visited.add(tmp)
        heappush(q, (move+1, ax, ay, tmp))
      nums[x + y*3], nums[ax + ay*3] = nums[ax + ay*3], nums[x + y*3]
      
print(-1)