N = int(input())

num_visited = [False]*100

num, cnt = N, 0

while not num_visited[num] :
  num_visited[num] = True
  _num = (num // 10 + num % 10)
  num = (num % 10) * 10 + _num % 10
  cnt += 1

print(cnt)