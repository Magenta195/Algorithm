from collections import deque

while True:
  n, *lst = map(int, input().split())
  if n == 0 : break

  ans = 0
  stk = deque([])
  for i in range(n):
    if not stk :
      stk.append((lst[i],i))
      continue
    h, j = stk[-1]
    if h < lst[i] :
      stk.append((lst[i],i))
    elif h > lst[i] :
      while stk and stk[-1][0] > lst[i]:
        h, j = stk.pop()
        ans = max(ans, h*(i-j))
      stk.append((lst[i],j))

  while stk:
    h, j = stk.pop()
    ans = max(ans, h*(n-j))
  print(ans)