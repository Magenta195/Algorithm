N = int(input())
num_list = list(map(int, input().split()))
stk = list()
result = [-1]*N

for i in range(N) :
  tmp = list()
  while stk and stk[-1][0] < num_list[i] :
    num, idx = stk.pop()
    tmp.append(idx)
  stk.append((num_list[i], i))
  for idx in tmp :
    result[idx] = num_list[i]

print(*result)