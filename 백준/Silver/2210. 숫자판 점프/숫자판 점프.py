
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

map_list = [input().split() for _ in range(5)]

q = list()
for i in range(5) :
  for j in range(5) :
    q.append((j, i, map_list[i][j]))

result = set()
while q :
  x, y, s = q.pop()
  if len(s) == 6 :
    result.add(s)
    continue
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < 5 and -1 < ay < 5 :
      q.append((ax, ay, s + map_list[ay][ax]))

print(len(result))