ans = [[0]*100 for i in range(100)]
for i in range(100) :
  ans[99-i][i] = i + 9901
cnt = 1
for i in range(100) :
  _range = range(100) if i % 2 == 0 else range(99, -1, -1)
  for j in _range :
    if ans[i][j] :
      continue
    ans[i][j] = cnt
    cnt += 1
for _ans in ans:
  print(*_ans)