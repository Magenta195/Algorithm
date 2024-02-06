import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
MAX = max(nums) + 1
parent = list(range(MAX))
result = [0]*MAX
is_prime = [True]*MAX
prime_factor = [[] for i in range(MAX)]

for i in range(2, MAX) :
  if not is_prime[i] :
    continue
  prime_factor[i].append(i)
  for j in range(i*2, MAX, i) :
    is_prime[j] = False
    prime_factor[j].append(i)

def find(a) :
  if a == parent[a] :
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(pa, pb) :
  if pa == pb :
    return
  if pa > pb :
    pa, pb = pb, pa
  parent[pb] = pa

for i in range(N) :
  p = MAX
  if is_prime[nums[i]] :
    result[find(nums[i])] += 1
    continue
  for j in prime_factor[nums[i]] :
    pj = find(j)
    if p > pj :
      p = pj
  for j in prime_factor[nums[i]] :
    union(p, find(j))
  result[p] += 1

for i in range(2, MAX) :
  if not is_prime[i] :
    continue
  pi = find(i)
  if i == pi :
    continue
  result[pi] += result[i]
  result[i] = 0
print(max(result))