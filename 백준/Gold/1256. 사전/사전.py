N, M, K = map(int, input().split())

combinations = [[0]*(N+M+1) for _ in range(N+M+1)]

combinations[0][0] = 1

for i in range(1, N+M+1) :
  for j in range(i+1) :
    if i == 0 or i == j :
      combinations[i][j] = 1
    else :
      combinations[i][j] = combinations[i-1][j-1] + combinations[i-1][j]

if combinations[N+M][N] < K :
  print(-1)
  exit()

answer = ''
left_a, left_k = N, K
for i in range(M-1, -1, -1) :
  for j in range(left_a, -1, -1) :
    if combinations[left_a-j+i][left_a-j] < left_k :
      left_k -= combinations[left_a-j+i][left_a-j]
    else :
      answer += 'a'*j
      left_a -= j
      break
  if left_k == 0 :
    break
  answer += 'z'

answer += 'a'*left_a
print(answer)