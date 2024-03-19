import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(K)]

def check_rules(target) :
  res = 0
  for a, b, c in rules :
    if target < a :
      continue
    b = min(b, target)
    res += (b - a) // c + 1
  return res >= D

def binary_search() :
  start, end = 0, N
  while start < end :
    mid = (start + end) // 2
    if check_rules(mid) :
      end = mid
    else :
      start = mid + 1
  return end

print(binary_search())