N = int(input())

map_list = [input().strip() for _ in range(N)]

rowcnt, colcnt = 0, 0
for i in range(N) :
  tmp_row_cnt, tmp_col_cnt = 0, 0
  for j in range(N) :
    if map_list[i][j] == '.' :
      tmp_row_cnt += 1
    else :
      if tmp_row_cnt > 1 :
        rowcnt += 1
      tmp_row_cnt = 0

    if map_list[j][i] == '.' :
      tmp_col_cnt += 1
    else :
      if tmp_col_cnt > 1 :
        colcnt += 1
      tmp_col_cnt = 0
  if tmp_row_cnt > 1 :
    rowcnt += 1
  if tmp_col_cnt > 1 :
    colcnt += 1

print(rowcnt, colcnt)