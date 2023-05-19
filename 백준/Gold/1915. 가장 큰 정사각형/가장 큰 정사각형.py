import sys
input = sys.stdin.readline

n, m = map(int, input().split())
square_list = [list(map(int, list(input().strip()))) for _ in range(n)]

for i in range(1, n) :
  for j in range(1, m) :
    if square_list[i][j] == 1 :
      square_list[i][j] += min(square_list[i][j-1], square_list[i-1][j], square_list[i-1][j-1])

print(max(map(max, square_list)) ** 2)