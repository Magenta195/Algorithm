N = int(input())
num_list = list(map(int, input().split()))
sum_list = [0]
for i in range(N) :
  sum_list.append(sum_list[-1] + num_list[i])

stk, ans = list(), 0

for i in range(N) :
  j = i
  while stk and stk[-1][0] >= num_list[i] :
    h, j = stk.pop()
    ans = max(ans, (sum_list[i] - sum_list[j])*h)
  stk.append((num_list[i], j))

while stk :
  h, j = stk.pop()
  ans = max(ans, (sum_list[-1] - sum_list[j])*h)

print(ans)