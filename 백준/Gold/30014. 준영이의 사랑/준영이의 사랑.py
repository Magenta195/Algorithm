from collections import deque

N = int(input())
pearls = sorted(map(int, input().split()), reverse = True)

lst = deque()

for i in range(N) :
  if i % 2 :
    lst.append(pearls[i])
  else :
    lst.appendleft(pearls[i])

ans = 0
for i in range(N) :
  ans += lst[i] * lst[(i+1)%N]
print(ans)
print(*lst)