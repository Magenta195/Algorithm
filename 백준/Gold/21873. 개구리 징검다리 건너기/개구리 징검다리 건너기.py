N = int(input())

print(N**2 + 2*N)
cnt = 0
for i in range(1, N+1) :
  for j in range(1, i+1) :
    print(cnt+1, j)
  cnt = 1-cnt
for i in range(1, N+1) :
  print(cnt+1, i)
cnt = 1-cnt
for i in range(1, N+1) :
  for j in range(i, N+1) :
    print(cnt+1, j)
  cnt = 1-cnt