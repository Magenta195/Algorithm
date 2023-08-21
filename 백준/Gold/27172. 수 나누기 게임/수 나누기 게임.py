MAX = 1000001
N = int(input())

nums = [-1]*MAX
num_list = list(map(int, input().split()))

for idx, num in enumerate(num_list) :
  nums[num] = idx

score_list = [0]*N

for i in range(MAX) :
  if nums[i] > -1 :
    tmp = i
    while tmp < MAX :
      if nums[tmp] > -1 :
        score_list[nums[i]] += 1
        score_list[nums[tmp]] -= 1
      tmp += i

print(*score_list)