from collections import Counter 
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

def is_enable() :
  if N % 2 :
    return False
  counter = Counter(nums)
  cnt = N
  minval = min(counter.keys())
  maxval = max(counter.keys())
  counter[minval] -= 1
  counter[maxval] -= 1
  
  for i in range(minval+1, maxval) :
    if counter[i] < 2 :
      return False
    counter[i] -= 2
  cnt -= (maxval - minval) * 2

  for i in range(minval, maxval) :
    if not counter[i] :
      continue
    if counter[i] > counter[i+1] :
      return False
    counter[i+1] -= counter[i]
    cnt -= counter[i] * 2
    counter[i] = 0
  return cnt == 0
print(1 if is_enable() else -1)