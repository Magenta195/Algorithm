import sys
input = sys.stdin.readline

N = int(input())
honor = [int(input()) for _ in range(N)]
honor.sort()
stk = [0]
ans = 0

for h in honor :
  if h - stk[-1] > 1 :
    ans += h-stk[-1]-1
    stk.append(stk[-1]+1)
  else :
    stk.append(h)
print(ans)