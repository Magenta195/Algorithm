import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
answer = []
stk = []

for i in range(N) :
  cur_min, cur_max = num_list[i], num_list[i]
  while stk and ( stk[-1][0] == cur_max + 1 or  stk[-1][1] == cur_min - 1) :
    prev_min, prev_max, prev_idx = stk.pop()
    cur_min = min(cur_min, prev_min)
    cur_max = max(cur_max, prev_max)
    answer.append(prev_idx + 1)
  stk.append((cur_min, cur_max, i))

cur_min, cur_max, cur_idx = stk.pop()
while stk :
  prev_min, prev_max, prev_idx = stk.pop()
  cur_min = min(cur_min, prev_min)
  cur_max = max(cur_max, prev_max)

print(*answer, sep = "\n")
