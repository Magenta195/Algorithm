S = input().strip()
T = input().strip()
q = [T]

while q :
  t = q.pop()
  if t == S :
    print(1)
    exit()
  if len(t) == len(S) :
    continue
  if t[-1] == 'A' :
    q.append(t[:-1])
  else :
    q.append(t[:-1][::-1])
print(0)