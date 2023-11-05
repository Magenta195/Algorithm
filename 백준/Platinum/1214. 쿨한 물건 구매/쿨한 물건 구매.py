D, P, Q = map(int, input().split())
if P < Q :
  P, Q = Q, P
  
ans = float('inf')
q = [0]

for i in range(0, D+P, P) :
  target = max(D - i, 0)
  tmp = target // Q * Q
  if tmp < target :
    tmp += Q

  if ans > tmp + i :
    ans = tmp + i
  elif ans == tmp + i :
    break

print(ans)