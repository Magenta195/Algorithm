from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cvt = lambda x : int(x) % M
num_list = list(map(cvt, input().split()))

mod_list = deque([0]*M)
sum_val = 0
for i in range(N) :
  sum_val = (sum_val + num_list[i]) % M
  mod_list[sum_val] += 1

answer = 0
for i in range(N) :
  answer += mod_list[0]
  mod_list[num_list[i]] -= 1
  mod_list.rotate(-num_list[i])

print(answer)