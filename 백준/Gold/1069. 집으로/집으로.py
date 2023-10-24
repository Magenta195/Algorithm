from collections import deque

X, Y, D, T = map(int, input().split())
dist = (X**2 + Y**2) ** 0.5

if D/T <= 1 :
  print(dist)
  exit()

direct = dist // D * T
answer = direct + min(dist % D, T + (D - dist % D), 2*T)
answer = min(answer, max(2*T, direct + T))
print(answer)