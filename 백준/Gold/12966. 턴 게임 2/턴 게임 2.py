MAX = float('inf')
x, y = map(int, input().split())
total = x + y
if total ** 0.5 % 1 != 0 :
  print(-1)
  exit()
if x == 0 :
  print(0)
  exit()
total = int(total ** 0.5)
cnt = 0

for i in range(total-1, -1, -1) :
  if x < 2*i+1 or x - 2*i - 1 == 2 :
    continue
  x -= 2*i + 1
  cnt += 1
  if x == 0 :
    break
print(cnt if not x else -1)