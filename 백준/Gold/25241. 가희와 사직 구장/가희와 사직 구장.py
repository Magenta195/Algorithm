from itertools import combinations
import sys
input = sys.stdin.readline

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

R, C, N = map(int, input().split())
_, _, _ = map(int, input().split())
synergy = sorted(map(int, input().split()), reverse = True)
maps = [list(map(int, input().split())) for _ in range(R)]
maps = [(maps[r][c], r*C+c) for r in range(R) for c in range(C)]
sorted_maps = sorted(maps, reverse=True)
used_set = set()
used_sum = 0
for i in range(N) :
  used_set.add(sorted_maps[i][1])
  used_sum += sorted_maps[i][0]
ans = 0

for combs in combinations(range(R*C), 3) :
  max_adj = 0
  used = []
  unused = []
  for i in range(3) :
    ir, ic = combs[i] // C, combs[i] % C
    jr, jc = combs[(i+1) % 3] // C, combs[(i+1) % 3] % C
    if abs(ir - jr) + abs(ic - jc) == 1 or abs(ir - jr) == abs(ic - jc) == 1 :
      max_adj += 1
    if combs[i] not in used_set :
      unused.append(combs[i])

  sums = used_sum + sum(synergy[:max_adj])
  idx, cnt = N-1, 0
  while cnt < len(unused) :
    if sorted_maps[idx][1] in combs :
      idx -= 1
      continue
    sums += maps[unused[cnt]][0] - sorted_maps[idx][0]
    idx -= 1
    cnt += 1

  ans = max(ans, sums)
print(ans)