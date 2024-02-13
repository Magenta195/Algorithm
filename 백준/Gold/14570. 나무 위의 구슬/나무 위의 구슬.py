import sys
input = sys.stdin.readline

N = int(input())
children = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
K = int(input()) - 1

node = 1
while True :
  if children[node][0] == children[node][1] == -1 :
    print(node)
    break
  if children[node][0] == -1 :
    node = children[node][1]
  elif children[node][1] == -1 :
    node = children[node][0]
  else :
    node, K = children[node][K % 2], K // 2