dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int,input().split())
order = []
x, y = N//2, N//2
c, cnt, dir = 0, 1, 0
blizaard = [[] for _ in range(5)]

while True:
  for _ in range(cnt):
    x, y = x+dx[dir], y+dy[dir]
    order.append((x, y))
    if x == 0 and y == 0 : break
    elif x == N//2 :
      if y > N//2 :
        blizaard[2].append(c)
      else :
        blizaard[1].append(c)
    elif y == N//2 :
      if x > N//2 :
        blizaard[4].append(c)
      else :
        blizaard[3].append(c)
    c += 1
        
  if x == 0 and y == 0 : break
  dir = (dir+1)%4
  for _ in range(cnt):
    x, y = x+dx[dir], y+dy[dir]
    order.append((x, y))
    if x == N//2 :
      if y > N//2 :
        blizaard[2].append(c)
      else :
        blizaard[1].append(c)
    elif y == N//2 :
      if x > N//2 :
        blizaard[4].append(c)
      else :
        blizaard[3].append(c)
    c += 1
  cnt += 1
  dir = (dir+1)%4

map_lst = [list(map(int,input().split())) for _ in range(N)]
lst = [map_lst[y][x] for x, y in order]
ans, end = 0, N**2-1
for _ in range(M):
  d, s = map(int,input().split())
  for i in range(s):
    lst[blizaard[d][i]] = 0
  lst.sort(key = lambda x : x == 0)

  while True:
    flg = True
    cnt, start, base = 1, 0, lst[0]
    for i in range(1, end):
      if base == lst[i] :
        cnt += 1
      else :
        if cnt >= 4 :
          flg = False
          ans += cnt*base
          for j in range(start, i):
            lst[j] = 0
        cnt, start, base = 1, i, lst[i]
      if lst[i] == 0: break
      if i == end-1 and cnt >= 4:
          flg = False
          ans += cnt*base
          for j in range(start, i+1):
            lst[j] = 0
    lst.sort(key = lambda x : x == 0)
    if flg : break
  tmp = []
  cnt, base = 1, lst[0]
  for i in range(1, end):
    if base == lst[i] :
      cnt += 1
    else :
      tmp += [cnt, base]
      cnt, base = 1, lst[i]
    if lst[i] == 0 : break
    if i == end-1 :
      tmp += [cnt, base]
  if len(tmp) < len(lst) :
    tmp += [0]*(len(lst)-len(tmp))
  elif len(tmp) > len(lst) :
    tmp = tmp[:end]
  lst = tmp
print(ans)