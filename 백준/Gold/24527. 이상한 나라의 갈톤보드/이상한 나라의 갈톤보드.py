import bisect
import sys
input = sys.stdin.readline

H = int(input())
Q, R = map(int, input().split())
sum_list = [0]
for i in range(H) :
  sum_list.append(sum_list[-1]+i+1)

updates = [0.]*(H+2)
for _ in range(Q) :
  a, b = map(int, input().split())
  idx = bisect.bisect_left(sum_list, a)
  start = a - sum_list[idx-1] - 1
  end = start + (H - idx + 1)
  updates[start] += b / (end - start + 1)
  updates[end+1] -= b / (end - start + 1)

result = [0.]*(H+2)
for i in range(1, H+2) :
  result[i] = result[i-1] + updates[i-1]
for i in range(1, H+2) :
  result[i] += result[i-1]

for _ in range(R) :
  a, b = map(int, input().split())
  print(result[b] - result[a-1])