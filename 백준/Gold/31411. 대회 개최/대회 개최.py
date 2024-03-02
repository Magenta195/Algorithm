import sys
input = sys.stdin.readline
MAX = 10**6+1

N, K = map(int, input().split())
index = set()
counter = [[] for _ in range(MAX)]

for i in range(N) :
  for j in map(int, input().split()) :
    counter[j].append(i)
    index.add(j)

index = sorted(index)
matched = 0
visited = [0]*N

def update(idx, mode) :
  global matched
  for c in counter[idx] :
    if mode == 1 :
      if not visited[c] :
        matched += 1
      visited[c] += 1
    else :
      visited[c] -= 1
      if not visited[c] :
        matched -= 1

l, r = 0, -1
ans = MAX
while r < len(index) :
  if matched < N :
    if r == len(index)-1 :
      break
    r += 1
    update(index[r], 1)
  else :
    ans = min(ans, index[r] - index[l])
    l += 1
    update(index[l-1], -1)
print(ans)