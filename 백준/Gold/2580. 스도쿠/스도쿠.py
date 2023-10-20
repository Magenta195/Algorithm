sudoku = [list(map(int, input().split())) for _ in range(9)]

empty_cells = list()

for i in range(9) :
  for j in range(9) :
    if sudoku[i][j] == 0 :
      empty_cells.append((j, i))

def check(x, y, num) :
  for i in range(9) :
    if sudoku[i][x] == num:
      return False
    if sudoku[y][i] == num:
      return False
  for i in range(y // 3 * 3, y // 3 * 3 + 3) :
    for j in range(x // 3 * 3, x // 3 * 3 + 3) :
      if sudoku[i][j] == num:
        return False
  return True

def dfs(idx) :
  if idx == len(empty_cells) :
    return True

  x, y = empty_cells[idx]
  for i in range(1, 10) :
    if check(x, y, i) :
      sudoku[y][x] = i
      result = dfs(idx+1)
      if result :
        return True
      sudoku[y][x] = 0
  return False
dfs(0)
for _sudoku in sudoku :
  print(*_sudoku)