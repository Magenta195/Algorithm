import sys
input = sys.stdin.readline

def find(a) :
  if a == parents[a] :
    return a

  pa = find(parents[a])
  dist[a] += dist[parents[a]]
  parents[a] = pa
  return pa

def solve() :
  global parents, dist
  N = int(input())
  parents = list(range(N+1))
  dist = [0]*(N+1)
  while True :
    q, *cmd = input().split()
    if q == 'E' :
      i = int(cmd[0])
      find(i)
      print(dist[i])
    elif q == 'I' :
      i, j = map(int, cmd)
      parents[i] = j
      dist[i] += abs(i - j) % 1000
    if q == 'O' :
      break
  del parents

for _ in range(int(input())) :
  solve()