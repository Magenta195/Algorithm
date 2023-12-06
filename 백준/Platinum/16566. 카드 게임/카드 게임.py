import sys
sys.setrecursionlimit(10000000)

N,M,K = map(int, input().split())
card = sorted(list(map(int, input().split())))
parent = list(range(M))
K_card = list(map(int, input().split()))

def find(a):
  if parent[a] == a:
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(a, a1):
  parent[a] = a1

for k in K_card :
  start, end = 0, M-1
  while start < end :
    mid = (start + end) // 2
    if card[mid] <= k :
      start = mid + 1
    else :
      end = mid
  v = find(end)
  if v < M-1 : v1 = find(v+1)
  print(card[v])
  if v < M-1 : union(v, v1)