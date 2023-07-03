import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]
heapify(num_list)
result = 0
while len(num_list) > 1 :
  a = heappop(num_list)
  b = heappop(num_list)
  result += a + b
  heappush(num_list, a+b)

print(result)