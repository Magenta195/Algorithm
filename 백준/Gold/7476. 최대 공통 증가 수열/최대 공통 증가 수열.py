N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

dp = [[[0, (-1, -1)] for j in range(M)] for i in range(N)]

for i in range(N) :
  for j in range(M) :
    if N_list[i] != M_list[j] :
      continue
    dp[i][j][0] += 1
    for k in range(i+1, N) :
      if N_list[i] >= N_list[k] :
        continue
      for l in range(j+1, M) :
        if M_list[l] == N_list[k] :
          if dp[k][l][0] < dp[i][j][0] :
            dp[k][l] = [ dp[i][j][0], (i, j) ]
          break

answer, answer_idx, answer_list = 0, (-1, -1), list()

for i in range(N) :
  for j in range(M) :
    if dp[i][j][0] > answer :
      answer, answer_idx = dp[i][j][0], (i, j)

while answer_idx != (-1, -1) :
  answer_list.append((N_list[answer_idx[0]]))
  answer_idx = dp[answer_idx[0]][answer_idx[1]][1]

print(answer)
print(*reversed(answer_list))