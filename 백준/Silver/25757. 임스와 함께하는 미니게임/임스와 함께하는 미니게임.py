import sys
input = sys.stdin.readline
player_set = set()
mode_type = {
  'Y' : 1, 'F' : 2, 'O' : 3
}
N, typ = input().split()
for _ in range(int(N)) :
  player_set.add(input().strip())
print(len(player_set) // mode_type[typ])