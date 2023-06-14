S = list(input().strip())

ones, zeros = 0, 0
for s in S :
  if s == '0' :
    zeros += 1
  else :
    ones += 1

ones //= 2
zeros //= 2
idx = len(S) - 1
while zeros :
  if S[idx] == '0' :
    S.pop(idx)
    zeros -= 1
  idx -= 1

idx = 0
while ones :
  if S[idx] == '1' :
    S.pop(idx)
    ones -= 1
  else :
    idx += 1

print(''.join(S))