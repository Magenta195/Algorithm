from collections import defaultdict
import sys
input = sys.stdin.readline

def find_string(K, W) :
  minval, maxval = len(W)+1, -1
  alphabet_dict = defaultdict(list)
  for i in range(len(W)) :
    alphabet_dict[W[i]].append(i)

  for idx_list in alphabet_dict.values() :
    if len(idx_list) < K :
      continue
    for i in range(len(idx_list)-K+1) :
      minval = min(minval, idx_list[i+K-1] - idx_list[i] + 1)
      maxval = max(maxval, idx_list[i+K-1] - idx_list[i] + 1)
  return minval, maxval

T = int(input())
for _ in range(T) :
  W = input().strip()
  K = int(input())
  minval, maxval = find_string(K, W)
  if maxval == -1 :
    print(maxval)
  else :
    print(minval, maxval)