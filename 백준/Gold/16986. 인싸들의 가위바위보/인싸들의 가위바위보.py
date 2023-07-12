import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, K = map(int, input().split())
winning_list = [list(map(int, input().split())) for _ in range(N)]
friend_list = [list(map(lambda x : int(x)-1, input().split())) for _ in range(2)]
visited = [False]*N

def dfs(f1, f2, idxs, winnings) :
  if winnings[0] == K :
    return True
  if winnings[1] == K or winnings[2] == K :
    return False
  if f1 != 0 and f2 != 0:
    b_act, c_act = friend_list[0][idxs[0]], friend_list[1][idxs[1]]
    if winning_list[b_act][c_act] == 2 :
      winner = 1
    else :
      winner = 2
    winnings[winner] += 1
    idxs = [ idx + 1 for idx in idxs ]
    return dfs(0, winner, idxs, winnings)

  for act in range(N) :
    if visited[act] :
      continue
    visited[act] = True
    next_winnings = winnings[:]
    next_idxs = idxs[:]
    if winning_list[act][friend_list[f2-1][idxs[f2-1]]] == 2:
      winner = 0
    else :
      winner = f2
    target = 1 if f2 == 2 else 2
    next_winnings[winner] += 1
    next_idxs[f2-1] += 1
    result = dfs(winner, target, next_idxs, next_winnings)
    if result :
      return True
    visited[act] = False
  return False

print(1 if dfs(0, 1, [0,0], [0,0,0]) else 0)