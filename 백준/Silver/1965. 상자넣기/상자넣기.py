N = int(input())
num_list = list(map(int, input().split()))

def lower_bound(target, lis_list) :
  start, end = 0, len(lis_list)

  while start < end :
    mid = (start + end) // 2
    if lis_list[mid] < target :
      start = mid + 1
    else :
      end = mid

  lis_list[end] = target

def full_search() :
  lis_list = [num_list[0]]
  for num in num_list[1:] :
    if lis_list[-1] < num :
      lis_list.append(num)
    else :
      lower_bound(num, lis_list)

  print(len(lis_list))

full_search()
      