import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

N = int(input())
children = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
K = int(input())

def dfs(node, k) :
  if children[node][0] == children[node][1] == -1 :
    return node
  if children[node][0] == -1 :
    return dfs(children[node][1], k)
  if children[node][1] == -1 :
    return dfs(children[node][0], k)

  if k % 2 == 0 :
    return dfs(children[node][0], k // 2)
  return dfs(children[node][1], k // 2)

print(dfs(1, K-1))