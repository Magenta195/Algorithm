dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


N = int(input())
lst = dict()
for _ in range(N**2):
  key, *val = map(int, input().split())
  lst[key] = val
cls = [[0]*N for _ in range(N)]
empty =[(i, j) for i in range(N) for j in range(N)]

for num in lst :
  tmp_lst = []
  for i, (x, y) in enumerate(empty):
    p, e = 0, 0
    for j in range(4):
      ax, ay = x+dx[j], y+dy[j]
      if -1<ax<N and -1<ay<N :
        if cls[ay][ax] in lst[num] :
          p += 1
        elif cls[ay][ax] == 0:
          e += 1
    tmp_lst.append((p, e, y, x, i))
  tmp_lst.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
  _, _, y, x, i = tmp_lst[0]
  del empty[i]
  cls[y][x] = num

ans = 0
for i in range(N):
  for j in range(N):
    cnt = 0
    num = cls[i][j]
    for k in range(4):
      if -1 < i+dy[k] < N and -1 < j+dx[k] < N and cls[i+dy[k]][j+dx[k]] in lst[num] :
        cnt += 1
    ans += 0 if cnt == 0 else 10**(cnt-1)
print(ans)
        