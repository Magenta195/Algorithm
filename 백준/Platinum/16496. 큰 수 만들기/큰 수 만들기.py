from functools import cmp_to_key

def cmp(a, b) :
  if a+b > b+a :
    return -1
  elif a+b == b+a :
    return 0
  else :
    return 1

N = int(input())
num_list = sorted(input().split(), key = cmp_to_key(cmp))
print(int("".join(num_list)))