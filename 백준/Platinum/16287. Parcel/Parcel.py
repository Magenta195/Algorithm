import sys
input = sys.stdin.readline
w, n = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
visited = [0]*(w+1)

def solve() :
  for i in range(len(n_list) + 1) :
    for j in range(i + 1, len(n_list)) :
      val = n_list[i] + n_list[j]
      if val > w :
        break
      visited[val] = (i, j)
  
  for i in range(len(n_list) + 1) :
    for j in range(i + 1, len(n_list)) :
      val = n_list[i] + n_list[j]
      if val > w :
        break
      if visited[w-val] and i not in visited[w-val] and j not in visited[w-val] :
        return True
  return False

print("YES" if solve() else "NO")