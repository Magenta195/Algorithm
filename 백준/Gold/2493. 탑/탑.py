N = int(input())
tower_list = list(map(int, input().split()))
answer_list = [0]*N
stk = list()

for idx, h in enumerate(reversed(tower_list)) :
  while stk and stk[-1][0] < h :
    _, pre = stk.pop()
    answer_list[pre-1] = N - idx
  stk.append((h, N - idx))

print(*answer_list)
