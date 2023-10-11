import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house_list = sorted([int(input()) for _ in range(N)])
start, end = 1, house_list[-1] - house_list[0]
answer = 0
while start <= end :
  mid = (start + end) // 2
  prev, cnt = house_list[0], 1
  for i in range(1, N) :
    if house_list[i] - prev >= mid :
      cnt += 1
      prev = house_list[i]
  if cnt >= C :
    answer = max(answer, mid)
    start = mid + 1
  else :
    end = mid - 1

print(answer)