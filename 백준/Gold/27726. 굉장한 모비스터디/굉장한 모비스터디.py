from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
M_list = list(map(int, input().split()))
p = [[i]*3 for i in range(N+1)]

def find(a, i) :
  if a == p[a][i] :
    return a
  p[a][i] = find(p[a][i], i)
  return p[a][i]

def union(a, b, i) :
  pa, pb = find(a, i), find(b, i)
  if pa > pb :
    pa, pb = pb, pa
  p[pb][i] = pa

for i in range(3) :
  for _ in range(M_list[i]) :
    a, b = map(int, input().split())
    union(a, b, i)
  for j in range(1, N+1) :
    find(j, i)

p = sorted([p[i] + [i] for i in range(1, N+1)])
ans = []
tmp = []
for i in range(N-1) :
  ta, a = tuple(p[i][:3]), p[i][3]
  tb, b = tuple(p[i+1][:3]), p[i+1][3]
  if ta == tb :
    if not tmp :
      tmp = [a, b]
    else :
      tmp.append(b)
  else :
    if tmp :
      ans.append(sorted(tmp))
    tmp = []
if tmp :
  ans.append(sorted(tmp))

ans.sort(key = lambda x : x[0])
print(len(ans))
for _ans in ans :
  print(*_ans)