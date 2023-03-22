N, K = map(int, input().split())
lst = list(map(int, input().split()))

def find_diff(A, B):
  diff = abs(A - B) // 5
  if diff > 0 :
    sign = 1 if A > B else -1
    return sign*diff
  return 0

cnt = 0
while max(lst) - min(lst) > K :
  m = min(lst)
  for i in range(N):
    if lst[i] == m : lst[i] += 1

  tmp = lst[1:]
  tmp_mat = [[lst[0]]]
  row, col, left = 1, 1, N-1
  while left >= col :
    tmp_mat = [[tmp_mat[i][j] for i in range(col-1,-1,-1)] for j in range(row)]
    row, col, left = col, row+1, left-col
    tmp_mat += [tmp[:row]]
    tmp = tmp[row:]

  dff_mat = [[0]*row for _ in range(col)]
  dff = [0]*left
  
  for y in range(col):
    for x in range(row):
      for dx, dy in [(0,1), (1,0)]:
        ax, ay = x+dx, y+dy
        if ax < row and ay < col :
          diff = find_diff(tmp_mat[y][x], tmp_mat[ay][ax])
          dff_mat[y][x] -= diff
          dff_mat[ay][ax] += diff
  if tmp :
    diff = find_diff(tmp_mat[-1][-1], tmp[0])
    dff_mat[-1][-1] -= diff
    dff[0] += diff
      
    for x in range(left-1):
      diff = find_diff(tmp[x], tmp[x+1])
      dff[x] -= diff
      dff[x+1] += diff
  
  for y in range(col):
    for x in range(row):
      tmp_mat[y][x] += dff_mat[y][x]
      
  if tmp :
    for x in range(left):
      tmp[x] += dff[x]
    
  lst = [[tmp_mat[i][j] for j in range(row) for i in range(col-1,-1,-1)] + tmp]

  row, col = N, 1
  for _ in range(2) :
    lst = [[lst[i][j] for j in range(row//2-1,-1,-1)] for i in range(col-1,-1,-1)] + [[lst[i][j] for j in range(row//2, row)] for i in range(col)]
    row, col = row//2, col*2

  dff_mat = [[0]*row for _ in range(col)]
  
  for y in range(col):
    for x in range(row):
      for dx, dy in [(0,1), (1,0)]:
        ax, ay = x+dx, y+dy
        if ax < row and ay < col :
          diff = find_diff(lst[y][x], lst[ay][ax])
          dff_mat[y][x] -= diff
          dff_mat[ay][ax] += diff
  for y in range(col):
    for x in range(row):
      lst[y][x] += dff_mat[y][x]
  lst = [lst[i][j] for j in range(row) for i in range(col-1,-1,-1)]

  cnt += 1
print(cnt)