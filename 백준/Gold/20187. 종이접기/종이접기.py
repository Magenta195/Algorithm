import sys
input = sys.stdin.readline

dx = [1, 0, 3, 2]
dy = [2, 3, 0, 1]

K = int(input())
length = 2**K
fold_list = list(reversed(input().split()))
h = int(input())
x, y = 1, 1
answer = [[h]]


for fold in fold_list :
  tmp = [[-1]*x for _ in range(y)]
  for i in range(y) :
    for j in range(x) :
      if fold in ['L', 'R'] :
        tmp[i][j] = dx[answer[i][x-j-1]]
      else :
        tmp[i][j] = dy[answer[y-i-1][j]]

  if fold == 'L' :
    for i in range(y) :
      answer[i] += tmp[i]
    x *= 2
  elif fold == 'R' :
    for i in range(y) :
      answer[i] = tmp[i] + answer[i]
    x *= 2
  elif fold == 'U' :
    answer += tmp
    y *= 2
  else :
    answer = tmp + answer
    y *= 2

for _answer in answer :
  print(*_answer)