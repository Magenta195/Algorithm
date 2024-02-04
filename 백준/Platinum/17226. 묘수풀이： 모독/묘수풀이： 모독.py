from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

minions =[]
total = { key : 0 for key in range(13) }
log = []
enemy_left = M

for i in range(N+M) :
  a, h = map(int, input().split())
  minions.append([a, h])
  total[h] += 1

def change_val(i, orig, changed) :
  minions[i][1] = changed
  total[orig] -= 1
  total[changed] += 1

def modok(n, md) :
  global enemy_left
  if md :
    return False
  dmg = 1
  for i in range(1, 13) :
    if not total[i] :
      break
    dmg += 1

  diff_list = []
  for i in range(N+M) :
    if not minions[i][1] :
      continue
    diff = max(0, minions[i][1] - dmg)
    diff_list.append((i, minions[i][1], diff))
    change_val(i, minions[i][1], diff)
    if i >= N and not diff :
      enemy_left -= 1
      
  log.append((0, 0))
  if dfs(n, 1) :
    return True
  log.pop()
  for i, orig, diff in diff_list :
    change_val(i, diff, orig)
    if i >= N and not diff :
      enemy_left += 1
  return False

def dfs(n, md) :
  global enemy_left
  if not enemy_left :
    return True
  if n == N :
    return modok(n, md)
  if dfs(n+1, md) :
    return True
  for i in range(M) :
    if not minions[i+N][1] :
      continue
    oa, oh = minions[perm[n]]
    ea, eh = minions[N+i]
    o_diff = max(oh-ea, 0)
    e_diff = max(eh-oa, 0)
    log.append((perm[n]+1, i+1))
    change_val(perm[n], oh, o_diff)
    change_val(N+i, eh, e_diff)
    if not e_diff :
      enemy_left -= 1
    if dfs(n+1, md) :
      return True
    if not e_diff :
      enemy_left += 1
    log.pop()
    change_val(perm[n], o_diff, oh)
    change_val(N+i, e_diff, eh)
  if n == N :
    return modok(n, md)
  return False

for perm in permutations(range(N)) :
  result = dfs(0, 0)
  if result :
    break
    
if not result :
  print("-1")
else :
  print(len(log)) 
  for i, j in log :
    if i :
      print("attack", i, j)
    else :
      print("use modok")