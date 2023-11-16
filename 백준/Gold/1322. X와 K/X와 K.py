x, k = map(int, input().split())
length = len(bin(x)[2:])
cnt = 1 << bin(x)[2:].count('0')

ans = 0
if k >= cnt :
  ans = (1 << length)*(k // cnt)
  k %= cnt

idx = 0
for i in range(length) :
  if not x & (1 << i) :
    if k & (1 << idx) :
      ans += (1 << i)
    idx += 1
print(ans)
