import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block_list = list(map(int, input().split()))

def valley_fill(left, right) :
  result = 0
  min_h = min(block_list[left], block_list[right])
  for i in range(left, right+1) :
    if block_list[i] < min_h :
      result += min_h - block_list[i]
      block_list[i] = min_h
  return result

def find_valleys() :
  result = 0
  top = -1
  disc = True
  for i in range(1, W) :
    if block_list[i-1] > block_list[i] :
      top = i-1
      break
  for j in range(i+1, W) :
    if block_list[j-1] > block_list[j] and not disc :
      result += valley_fill(top, j-1)
      top = j-1
      disc = True
    elif block_list[j-1] < block_list[j] and disc :
      disc = False

  if not disc :
    result += valley_fill(top, W-1)
  return result

answer = 0
while True :
  tmp = find_valleys()
  if not tmp :
    break
  answer += tmp

print(answer)