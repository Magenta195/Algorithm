from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
child_dict = defaultdict(list)
visited = [False]*N
ans = 0

for node, parent in enumerate(map(int, input().split())) :
  if parent != -1 :
    child_dict[parent].append(node)
  else :
    root = node

def dfs(node) :
  global ans
  tmp = 0
  for child in child_dict[node] :
    if not visited[child] :
      dfs(child)
      tmp += 1
  if not tmp :
    ans += 1
  
visited[int(input())] = True
if not visited[root] :
  dfs(root)
print(ans)