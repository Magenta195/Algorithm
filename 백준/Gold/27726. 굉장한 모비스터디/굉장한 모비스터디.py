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

p = sorted([[tuple(p[i]), i] for i in range(1, N+1)])
ans = []
tmp, prev = [p[0][1]], p[0][0]
for i in range(1, N) :
  if prev == p[i][0] :
    tmp.append(p[i][1])
  else :
    if len(tmp) > 1 :
      ans.append(sorted(tmp))
    tmp, prev = [p[i][1]], p[i][0]
if len(tmp) > 1 :
  ans.append(sorted(tmp))

print(len(ans))
for _ans in sorted(ans) :
  print(*_ans)