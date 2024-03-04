N = int(input())
seq = [*map(int,input().split())]

S = [];
MAX = 0
for i in range(N):
  if MAX==i:
    S.append([])
  n = seq[i]
  MAX = max(MAX,n)
  S[-1].append(i+1)
print(len(S))
for s in S:
  print(len(s),*s)