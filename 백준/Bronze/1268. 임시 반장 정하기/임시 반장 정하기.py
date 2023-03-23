N = int(input())

friend_count = [0]*N
student_list = [list(map(int, input().split())) for _ in range(N)]

def compare(i, j) :
  for k in range(5) :
    if student_list[i][k] == student_list[j][k] :
      return 1
  return 0

for i in range(N-1) :
  for j in range(i+1, N) :
    num = compare(i, j)
    friend_count[i] += num
    friend_count[j] += num

answer, answer_val = 0, -1

for i in range(N) :
  if friend_count[i] > answer_val :
    answer, answer_val = i+1, friend_count[i]

print(answer)
  