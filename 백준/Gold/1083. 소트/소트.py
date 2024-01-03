N = int(input())
nums = list(map(int, input().split()))
S = int(input())
idx = 0
while S and idx < N-1:
  bidx = idx
  for i in range(idx+1, min(idx+S+1, N)) :
    if nums[bidx] < nums[i] :
      bidx = i
  for i in range(bidx-1, idx-1, -1) :
    nums[i], nums[i+1] = nums[i+1], nums[i]
  S -= bidx - idx
  idx += 1

print(*nums)