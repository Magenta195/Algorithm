import sys
input = sys.stdin.readline

N, M = map(int, input().split())
play_time = list(map(int, input().split()))

start, end = 0, N*30
val = float('inf')
while start < end :
  mid = (start + end) // 2
  tmp = 0
  for t in play_time :
    tmp += mid // t + 1
  if tmp < N :
    start = mid + 1
  else :
    end = mid
    val = min(val, tmp)

for i in range(M-1, -1, -1) :
  if end % play_time[i] == 0 :
    if val == N :
      print(i+1)
      break
    val -= 1
