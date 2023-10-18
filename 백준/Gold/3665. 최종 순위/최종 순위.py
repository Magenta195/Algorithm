import sys
input = sys.stdin.readline

def solve() :
  impossible = False
  unable = False
  
  n = int(input())
  t_list = list(map(int, input().split()))
  orig_set = [[set(), i] for i in range(n+1)]
  
  for i in range(n-1) :
    for j in range(i+1, n) :
      orig_set[t_list[i]][0].add(t_list[j])
  
  m = int(input())
  for _ in range(m) :
    a, b = map(int, input().split())
    if b in orig_set[a][0] : # b > a
      orig_set[a][0].discard(b)
      orig_set[b][0].add(a)
    elif a in orig_set[b][0] : # b < a 
      orig_set[a][0].add(b)
      orig_set[b][0].discard(a)
    else :
      impossible = True

  orig_set.sort(key = lambda x : (-len(x[0]), -x[1]))
  answer = list()
  for i in range(n) :
    if  len(orig_set[i][0]) != n-i-1 :
      impossible = True
      break
    answer.append(orig_set[i][1])
  if not impossible :
    print(*answer)
  else :
    print("IMPOSSIBLE")

for _ in range(int(input())) :
  solve()