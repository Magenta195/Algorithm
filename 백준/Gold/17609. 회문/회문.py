from collections import deque

T = int(input())

for _ in range(T) :
  str = input().strip()
  cnt = 0
  q = deque([(0, len(str)-1, 0)])
  result = 2
  
  while q :
    left, right, cnt = q.popleft()
    print
    if cnt > 2 :
      continue
    if left > right :
      result = min(result, cnt)
      continue
    if str[left] == str[right] :
      q.append((left+1, right-1, cnt))
    else :
      if str[left+1] == str[right] :
        q.append((left+2, right-1, cnt+1))
      if str[left] == str[right-1] :
        q.append((left+1, right-2, cnt+1))
  
  print(result)