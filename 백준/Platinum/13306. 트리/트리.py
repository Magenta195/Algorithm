import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

union_target = [0]*(N+1)
parents = list(range(N+1))
for i in range(2, N+1) :
  ui = int(input())
  union_target[i] = ui

ans = list()

def find(a) :
  if a == parents[a] :
    return a
  parents[a] = find(parents[a])
  return parents[a]

def union(a, b) :
  parents[b] = a
  
queries = [list(map(int, input().split())) for _ in range(N-1+Q)]
for q in reversed(queries) :
  if q[0] == 0 :
    b = q[1]
    a = find(union_target[b])
    union(a, b)
  else :
    a, b = q[1:]
    ans.append("YES" if find(a) == find(b) else "NO")

print(*reversed(ans), sep = "\n")
    