from collections import Counter
MAXVAL = 1001

N = int(input())

num_maps = [0]*1001
for key, val in  Counter(map(int, input().split())).items() :
  num_maps[key] = val

ans = list()

for i in range(MAXVAL) :
  if not num_maps[i] :
    continue
  if i == MAXVAL-1 or i < MAXVAL-1 and not num_maps[i+1] :
    ans += [i]*num_maps[i]
    continue
  if i < MAXVAL-2 :
    if not num_maps[i+2] :
      best_idx = -1
      for j in range(i+3, MAXVAL) :
        if num_maps[j] :
          best_idx = j
          break
      if best_idx != -1 :
        ans += [i]*num_maps[i] + [best_idx]
        num_maps[best_idx] -= 1
      else :
        ans += [i+1]*num_maps[i+1] + [i]*num_maps[i]
        num_maps[i+1] = 0
    else :
      ans += [i]*num_maps[i] + [i+2]
      num_maps[i+2] -= 1
  else :
    ans += [i+1]*num_maps[i+1] + [i]*num_maps[i]
    num_maps[i+1] = 0

print(*ans)