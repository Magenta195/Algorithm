import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
visited = [[False]*C for _ in range(R)]
k = int(input())

for _ in range(k) :
  br, bc = map(int, input().split())
  visited[br][bc] = True

sr, sc = map(int, input().split())
visited[sr][sc] = True
so = 0
order = list(map(lambda x : int(x)-1, input().split()))

flg = True
while flg :
  flg = False
  for i in range(4) :
    ao = (so + i) % 4
    ar, ac = sr + dr[order[ao]], sc + dc[order[ao]]
    if -1 < ar < R and -1 < ac < C and not visited[ar][ac] :
      sr, sc, so = ar, ac, ao
      visited[sr][sc] = True
      flg = True
      break
print(sr, sc)