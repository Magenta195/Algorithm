map_list = [[0]*101 for _ in range(101)]

def solve() :
  for _ in range(4) :
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2) :
      for x in range(x1, x2):
        map_list[y][x] = 1

  print(sum(map(sum, map_list)))

solve()