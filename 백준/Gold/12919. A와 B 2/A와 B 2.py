from collections import deque

S = input().strip()
T = input().strip()

q = deque([T])

while q :
  x = q.pop()
  if x == S :
    print(1)
    exit()
  if len(x) == len(S) :
    continue
  if x[-1] == 'A' :
    q.append(x[:-1])
  if x[0] == 'B' :
    q.append(x[1:][::-1])
print(0)