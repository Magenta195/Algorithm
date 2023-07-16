from collections import defaultdict
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
member_dict = dict()
team_dict = defaultdict(list)

for _ in range(N) :
  team = input().strip()
  num = int(input())
  for _ in range(num) :
    member = input().strip()
    team_dict[team].append(member)
    member_dict[member] = team
  team_dict[team].sort()

for _ in range(M) :
  string = input().strip()
  typ = int(input())
  if typ == 0 :
    for member in team_dict[string] :
      print(member)
  else :
    print(member_dict[string])