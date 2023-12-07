N = int(input())

str_list = [input().strip() for _ in range(N)]

def merge(n, lst) :
  if n == 0 :
    return ''
  if n == 1 :
    return lst[0]

  mid = n // 2
  str1 = merge(mid, lst[:mid])
  str2 = merge(n - mid, lst[mid:])
  result = ''

  while str1 or str2 :
    if len(str1) < len(str2) :
      str1, str2 = str2, str1
    if str2 == '' :
      result += str1
      break
    if str1 == '' :
      result += str2
      break
    if str2 < str1[:len(str2)] :
      result += str2[0]
      str2 = str2[1:]
    else :
      result += str1[0]
      str1 = str1[1:]

  return result

print(merge(N, str_list))