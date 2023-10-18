import sys
input = sys.stdin.readline

def solve() :
  impossible = False
  unable = False
  
  n = int(input())
  t_list = list(map(int, input().split()))
  orig_set = [[set() for _ in range(2)] + [i] for i in range(n+1)]
  
  for i in range(n-1) :
    for j in range(i+1, n) :
      orig_set[t_list[i]][1].add(t_list[j])
      orig_set[t_list[j]][0].add(t_list[i])
  
  m = int(input())
  for _ in range(m) :
    a, b = map(int, input().split())
    if b in orig_set[a][1] : # b > a
      orig_set[a][1].discard(b)
      orig_set[a][0].add(b)
      orig_set[b][0].discard(a)
      orig_set[b][1].add(a)
    elif a in orig_set[b][1] : # b < a 
      orig_set[a][0].discard(b)
      orig_set[a][1].add(b)
      orig_set[b][1].discard(a)
      orig_set[b][0].add(a)
    else :
      impossible = True

  orig_set.sort(key = lambda x : (len(x[0]), len(x[1])))
  answer = list()
  for i in range(n) :
    if len(orig_set[i+1][0]) != i or len(orig_set[i+1][1]) != n-i-1 :
      impossible = True
      break
    answer.append(orig_set[i+1][2])
  if not impossible :
    print(*answer)
  else :
    print("IMPOSSIBLE")

for _ in range(int(input())) :
  solve()