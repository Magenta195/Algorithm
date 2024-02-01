from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
word_set = set(''.join(words))
wlen = len(word_set)
next_s = { key : [] for key in word_set }
required = { key : 0 for key in word_set }
visited = { key : -1 for key in word_set }
q = deque()

enable = True
sortable = True
ans = ''

for i in range(N-1) :
  a, b = words[i], words[i+1]
  if a == b :
    continue
  length = min(len(a), len(b))
  flg = False
  for j in range(length) :
    if a[j] != b[j] :
      flg = True
      break
  if not flg :
    if len(a) > len(b) :
      enable = False
      break
    continue
  required[b[j]] += 1
  next_s[a[j]].append(b[j])

for w in word_set :
  if not required[w] :
    visited[w] = 0
    q.append((w, 0))

while q and enable :
  w, d = q.popleft()
  for next_w in next_s[w] :
    if visited[next_w] > -1 :
      enable = False
      break
    required[next_w] -= 1
    if not required[next_w] :
      visited[next_w] = d+1
      q.append((next_w, d+1))

if -1 in visited.values() :
  enable = False
if enable :
  visited = sorted(visited.items(), key = lambda x : x[1])
  for i in range(wlen) :
    w, d = visited[i]
    if d != i :
      sortable = False
      break
    ans += w

if not enable :
  print('!')
elif not sortable :
  print('?')
else :
  print(ans)