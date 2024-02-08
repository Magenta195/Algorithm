import sys
input = sys.stdin.readline

N, M = map(int, input().split())

orig = list(map(int, input().split()))
target = list(map(int, input().split()))

log = []
orig_order = sorted([(-x, i) for i, x in enumerate(orig)])
maxidx = target.index(max(target))

for i in range(N) :
  if not orig_order[i][0] :
    break
  if orig_order[i][1] == maxidx :
    continue
  log.append('+ {} {}'.format(maxidx+1, -orig_order[i][0]))

for i in range(N) :
  if i == maxidx or not target[i] :
    continue
  log.append('+ {} {}'.format(i+1, target[i]))

print(len(log))
print(*log, sep='\n')