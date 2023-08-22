import sys
input = sys.stdin.readline

C, N = map(int, input().split())
endpoint = '!'

color_dict = dict()
name_set = set()

for _ in range(C) :
  color = input().strip()
  cur_dict = color_dict
  for c in color :
    if c not in cur_dict :
      cur_dict[c] = dict()
    cur_dict = cur_dict[c]
  cur_dict[endpoint] = True

for _ in range(N) :
  name = input().strip()
  name_set.add(name)

Q = int(input())
for _ in range(Q) :
  team = input().strip()
  length = len(team)
  q = [[0, color_dict]]
  enable = False

  while q :
    idx, cur_dict = q.pop()
    if 0 < idx < length and endpoint in cur_dict and team[idx:] in name_set :
      enable = True
      break
    if idx < length and team[idx] in cur_dict :
      q.append([idx+1, cur_dict[team[idx]]])

  print('Yes' if enable else 'No')