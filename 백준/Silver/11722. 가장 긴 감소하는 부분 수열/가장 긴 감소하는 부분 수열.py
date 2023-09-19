N = int(input())
num_list = list(map(int, input().split()))
answer_list = list()

def binary_search(num) :
  start, end = 0, len(answer_list)
  while start < end :
    mid = (start + end) // 2
    if num < answer_list[mid] :
      start = mid + 1
    else :
      end = mid

  return end

for num in num_list :
  idx = binary_search(num)
  if idx == len(answer_list) :
    answer_list.append(num)
  else :
    answer_list[idx] = num

print(len(answer_list))