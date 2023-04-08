import sys
sys.setrecursionlimit(100000)

N = int(input())
visited = [[-1]*2 for _ in range(N+1)]

def play(left, mode):
  if visited[left][mode] > -1 :
    return visited[left][mode] > 0
    
  win_cnt = 0
  if left >= 1 and not play(left-1, 1-mode) :
      win_cnt += 1
  if left >= 3 and not play(left-3, 1-mode) :
      win_cnt += 1

  visited[left][mode] = win_cnt
  return win_cnt > 0

def solve():
  result = play(N, 0)
  print('SK' if result else 'CY')

solve()