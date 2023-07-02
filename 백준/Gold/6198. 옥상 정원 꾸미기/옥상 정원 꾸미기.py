import sys
input = sys.stdin.readline

N = int(input())
ans = 0
stk = list()
for i in range(N) :
  h = int(input())
  while stk and stk[-1][0] <= h :
    _h, idx = stk.pop()
    ans += i-idx
  stk.append((h, i))
while stk :
  _, idx = stk.pop()
  ans += N-idx
print(ans-N)