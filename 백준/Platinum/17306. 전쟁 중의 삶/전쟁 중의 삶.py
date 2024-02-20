N = int(input())
nums = list(map(int, input().split()))
visit = set()

def find_lca(a, b) :
  ad = len(bin(a))-2
  bd = len(bin(b))-2
  visit.add(a)
  visit.add(b)
  if ad > bd :
    a, b = b, a
  for _ in range(abs(bd - ad)) :
    b >>= 1
    visit.add(b)
  while a != b :
    a, b = a >> 1, b >> 1
    visit.add(a)
    visit.add(b)
  return a

root = find_lca(nums[0], nums[1])
for i in range(2, N) :
  root = find_lca(root, nums[i])

print(len(visit))