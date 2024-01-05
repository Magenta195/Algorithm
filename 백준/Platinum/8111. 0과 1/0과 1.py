from collections import deque

def solve() :
  N = int(input())
  visited = [[(-1, -1)]*N for _ in range(101)]
  visited[1][1%N] = (1, N)
  q = deque([(1, 1%N)])

  while q :
    length, left = q.popleft()
    if not left :
      result = ''
      for i in range(length, 0, -1) :
        val, left = visited[i][left]
        result += str(val)
      print(result[::-1])
      return
    if length == 100 :
      continue

    for n in range(2) :
      new_left = (left * 10 + n) % N
      if visited[length+1][new_left][0] == -1 :
        visited[length+1][new_left] = (n, left)
        q.append((length+1, new_left))
  return

for _ in range(int(input())) :
  solve()
  