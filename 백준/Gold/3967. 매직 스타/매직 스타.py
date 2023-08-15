import sys
sys.setrecursionlimit(100000)

star_list = [0]*12
visited = [False]*13
line_list = [
  (0, 2, 5, 7),
  (0, 3, 6, 10),
  (7, 8, 9, 10),
  (1, 2, 3, 4),
  (1, 5, 8, 11),
  (4, 6, 9, 11)
]
coord_list = [
  (4, 0), (1, 1), (3, 1), (5, 1), (7, 1),
  (2, 2), (6, 2), (1, 3), (3, 3), (5, 3), (7, 3),
  (4, 4)
]
map_list = [input().strip() for _ in range(5)]
result = [['.']*9 for _ in range(5)]

def check(idx) :
  for line in line_list :
    if line[-1] >= idx : 
      continue
    tmp = 0
    for l in line :
      tmp += star_list[l]
      
    if tmp != 26 :
      return False
  return True
  
def encode() :
  for i in range(12) :
    x, y = coord_list[i]
    if map_list[y][x] != 'x' :
      star_list[i] = ord(map_list[y][x]) - ord('A') + 1
      visited[star_list[i]] = True

def decode() :
  for i in range(12) :
    x, y = coord_list[i]
    result[y][x] = chr(ord('A') + star_list[i] - 1)
  for _result in result :
    print(''.join(_result))

def dfs(idx) :
  if idx in [5, 8, 11, 12] :
    if not check(idx) :
      return False
    if idx == 12 :
      decode()
      return True
  if star_list[idx] > 0 :
    return dfs(idx+1)
  for i in range(1, 13) :
    if visited[i] :
      continue
    star_list[idx] = i
    visited[i] = True
    tmp = dfs(idx+1)
    if tmp :
      return True
    star_list[idx] = 0
    visited[i] = False
  return False

encode()
dfs(0)