N, M, K = map(int, input().split())
K_list = list(map(int, input().split()))

def arrange_judge(length) :
  visit = [0]*K
  cnt = 1
  prev = K_list[0]
  visit[0] = 1

  for i in range(1, K) :
    if K_list[i] - prev >= length :
      cnt += 1
      visit[i] = 1
      prev = K_list[i]
    if cnt == M :
      break
  return cnt, visit

def binary_search() :
  start, end = 0, N+1
  result = []
  while start < end :
    mid = (start + end) // 2
    cnt, visit = arrange_judge(mid)
    if cnt == M :
      result = visit
      start = mid + 1
    else :
      end = mid
  print(''.join(map(str, result)))

binary_search()