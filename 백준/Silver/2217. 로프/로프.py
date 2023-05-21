import sys
input = sys.stdin.readline
N = int(input())
node_list = [int(input()) for _ in range(N)]
node_list.sort(reverse=True)
result = 0

for i in range(N) :
  result = max(result, node_list[i] * (i+1))

print(result)