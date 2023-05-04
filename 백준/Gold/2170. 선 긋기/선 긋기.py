import sys
input = sys.stdin.readline

N = int(input())
n_list = [list(map(int, input().split())) for _ in range(N)]
n_list.sort(key = lambda x : (x[0], -x[1]))

result = 0

prev_x, prev_y = n_list[0]
for x, y in n_list[1:] :
  if prev_y < x :
    result += prev_y - prev_x
    prev_x, prev_y = x, y
  elif prev_y < y :
    prev_y = y

print(result + prev_y - prev_x)