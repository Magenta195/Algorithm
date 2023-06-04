MAX = float('inf')
N = int(input())
nums = list(input().strip())
target = list(input().strip())
nums = list(map(int, nums))
target = list(map(int, target))

def search(cnt, nums, target) :
  for i in range(1, N) :
    if nums[i-1] != target[i-1] :
      nums[i-1] = 1 - nums[i-1]
      nums[i] = 1 - nums[i]
      if i < N-1 :
        nums[i+1] = 1 - nums[i+1]
      cnt += 1
  return cnt if nums[-1] == target[-1] else MAX

_nums = nums.copy()
for i in range(2) :
  _nums[i] = 1 - _nums[i]

result = MAX
result = min(search(0, nums.copy(), target.copy()), result)
result = min(search(1, _nums, target.copy()), result)

print(result if result < MAX else -1)
