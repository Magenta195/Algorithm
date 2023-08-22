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
  cur_dict = color_dict
  enable = False
  for i in range(length) :
    if endpoint in cur_dict and team[i:] in name_set :
      enable = True
      break
    if team[i] not in cur_dict :
      break
    cur_dict = cur_dict[team[i]]

  print('Yes' if enable else 'No')