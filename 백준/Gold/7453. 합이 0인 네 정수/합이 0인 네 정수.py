import sys

N = int(input())
num_list = [list() for _ in range(4)]

for _ in range(N) :
  for i, num in enumerate(map(int, input().split())) :
    num_list[i].append(num)

new_num_list = [list() for _ in range(2)]

for i in range(N) :
  for j in range(N) :
    for k in range(2) :
      new_num_list[k].append(num_list[2*k][i] + num_list[2*k+1][j])

for i in range(2) :
  new_num_list[i].sort()

answer, i, j = 0, 0, N**2-1

while i < N**2 and j > -1 :
  if new_num_list[0][i] + new_num_list[1][j] == 0 :
    ti, tj = i, j
    while i < N**2 and new_num_list[0][ti] == new_num_list[0][i] :
      i += 1
    while j > -1 and new_num_list[1][tj] == new_num_list[1][j] :
      j -= 1
    answer += (i - ti) * (tj - j)
  elif new_num_list[0][i] + new_num_list[1][j] > 0 :
    j -= 1
  else :
    i += 1
    
print(answer)