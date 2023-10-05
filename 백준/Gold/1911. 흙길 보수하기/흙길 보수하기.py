import math
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
hole_list = [list(map(int, input().split())) for _ in range(N)]
hole_list.sort(key = lambda x : (x[0], -x[1]))
prev = -L-1
answer = 0

for s, e in hole_list :
  if prev < s :
    answer += 1
    prev = s + L
  if prev < e :
    tmp = math.ceil((e - prev) / L)
    answer += tmp
    prev += L*tmp
    
print(answer)