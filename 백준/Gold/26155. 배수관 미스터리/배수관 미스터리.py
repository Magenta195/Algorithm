import sys
input = sys.stdin.readline

N, M = map(int, input().split())
querys = []
parents = list(range(N+1))
cnt = N

def find(a) :
  if parents[a] == a :
    return a
  parents[a] = find(parents[a])
  return parents[a]

def union(a, b) :
  global cnt
  pa, pb = find(a), find(b)
  if pa == pb :
    return
  if pa > pb :
    pa, pb = pb, pa
  parents[pb] = pa
  cnt -= 1

for _ in range(M) :
  a, b, c = input().split()
  querys.append((float(c), 0, int(a), int(b)))

Q = int(input())
ans = [0]*Q
for i in range(Q) :
  c = float(input())
  querys.append((c, 1, i))

querys.sort(key = lambda x : (-x[0], x[1]))
for _, q, *cmd in querys :
  if q == 0 :
    union(cmd[0], cmd[1])
  else :
    ans[cmd[0]] = cnt
    
print(*ans, sep = '\n')