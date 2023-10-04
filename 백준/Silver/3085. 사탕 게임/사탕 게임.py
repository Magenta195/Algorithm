import sys

N = int(input())
map_list = [list(input().strip()) for _ in range(N)]

def check_longest() :
  result = 1
  for i in range(N) :
    rtarget, rcnt = map_list[i][0], 1
    wtarget, wcnt = map_list[0][i], 1 
    for j in range(1, N) :
      if rtarget == map_list[i][j] :
        rcnt += 1
      else :
        result = max(result, rcnt)
        rtarget, rcnt = map_list[i][j], 1
      if wtarget == map_list[j][i] :
        wcnt += 1
      else :
        result = max(result, wcnt)
        wtarget, wcnt = map_list[j][i], 1
    result = max(result, rcnt, wcnt)
  return result

answer = 0
for i in range(N) :
  for j in range(N-1) :
    map_list[i][j], map_list[i][j+1] = map_list[i][j+1], map_list[i][j]
    answer = max(answer, check_longest())
    map_list[i][j], map_list[i][j+1] = map_list[i][j+1], map_list[i][j]
    map_list[j][i], map_list[j+1][i] = map_list[j+1][i], map_list[j][i]
    answer = max(answer, check_longest())
    map_list[j][i], map_list[j+1][i] = map_list[j+1][i], map_list[j][i]
print(answer)