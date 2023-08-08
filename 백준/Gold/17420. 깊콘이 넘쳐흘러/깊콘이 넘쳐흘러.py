N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

tot_list = [[a, b] for (a, b) in zip(a_list, b_list)]
tot_list.sort(key = lambda x : x[1])
result = 0
for i in range(N) :
  a, b = tot_list[i]
  if a < b :
    ext = (b - a) // 30 + 1
    result += ext
    a += ext * 30
  for j in range(i+1, N) :
    if tot_list[j][0] < a and tot_list[j][1] > b :
      if (a - tot_list[j][0]) % 30 :
        ext = (a - tot_list[j][0]) // 30 + 1
      else :
        ext = (a - tot_list[j][0]) // 30
      result += ext
      tot_list[j][0] += ext*30
print(result)