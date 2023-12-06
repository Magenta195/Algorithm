import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

def div_and_conqure(start, end) :
  if start == end :
    return 0

  mid = (start + end) // 2
  left = div_and_conqure(start, mid)
  right = div_and_conqure(mid+1, end)
  result = 0
  
  l, r = start, mid+1
  temp = list()
  while l < mid+1 and r < end+1 :
    if num_list[l] < num_list[r] :
      temp.append(num_list[l])
      l += 1
    else :
      temp.append(num_list[r])
      r += 1
      result += mid - l + 1

  for i in range(l, mid+1) :
    temp.append(num_list[i])
  for i in range(r, end+1) :
    temp.append(num_list[i])
  
  for i in range(end - start + 1) :
    num_list[i+start] = temp[i]

  return result + left + right

print(div_and_conqure(0, N-1))