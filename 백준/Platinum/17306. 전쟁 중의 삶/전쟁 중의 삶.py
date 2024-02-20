N = int(input())
nums = list(map(int, input().split()))

def find_lca(a, b) :
  ad = len(bin(a)) - 2
  bd = len(bin(b)) - 2
  if ad > bd :
    a, ad, b, bd = b, bd, a, ad
  for _ in range(bd - ad) :
    b >>= 1
  while a != b :
    a >>= 1
    b >>= 1
  return a

root = find_lca(nums[0], nums[1])
for i in range(2, N) :
  root = find_lca(root, nums[i])

visit = {root}
for n in nums :
  while n != root :
    visit.add(n)
    n >>= 1

print(len(visit))