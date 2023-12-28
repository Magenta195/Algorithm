from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
sqrt = N ** 0.5
nums = list(map(int, input().split()))
M = int(input())
ans = [0]*M

queries = [[i] + list(map(int, input().split())) for i in range(M)]
queries.sort(key = lambda x : (x[1] // sqrt, x[2]))

num_list = defaultdict(int)
cnt, prev_i, prev_j = 0, 0, -1
table = [0]*(N+2)
table[0] = N
for idx, i, j in queries :
  i -= 1
  j -= 1
  while prev_j < j :
    prev_j += 1
    table[num_list[nums[prev_j]]] -= 1
    num_list[nums[prev_j]] += 1
    table[num_list[nums[prev_j]]] += 1
    cnt = max(num_list[nums[prev_j]], cnt)
  while prev_j > j :
    table[num_list[nums[prev_j]]] -= 1
    if cnt == num_list[nums[prev_j]] and not table[cnt] :
      cnt -= 1
    num_list[nums[prev_j]] -= 1
    table[num_list[nums[prev_j]]] += 1
    prev_j -= 1
  while prev_i < i :
    table[num_list[nums[prev_i]]] -= 1
    if cnt == num_list[nums[prev_i]] and not table[cnt] :
      cnt -= 1
    num_list[nums[prev_i]] -= 1
    table[num_list[nums[prev_i]]] += 1
    prev_i += 1
  while prev_i > i :
    prev_i -= 1
    table[num_list[nums[prev_i]]] -= 1
    num_list[nums[prev_i]] += 1
    table[num_list[nums[prev_i]]] += 1
    cnt = max(num_list[nums[prev_i]], cnt)
  ans[idx] = cnt
print(*ans, sep = '\n')