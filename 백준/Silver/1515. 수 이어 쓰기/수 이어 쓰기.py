num_list = input().strip()
pnt = 0
cnt = 1

def isin(num, cnt) :
  if not num :
    return True
  if not cnt :
    return False
  if num[0] == cnt[0] :
    return isin(num[1:], cnt[1:])
  return isin(num, cnt[1:])

while pnt < len(num_list) :
  num = num_list[pnt]
  while True :
    if num in str(cnt) :
      break
    cnt += 1
  tmp = 1

  while pnt + tmp < len(num_list) :
    num += num_list[pnt+tmp]
    if not isin(num, str(cnt)) or len(num) > len(str(cnt)):
      break
    tmp += 1
  pnt += tmp
  cnt += 1
print(cnt-1)