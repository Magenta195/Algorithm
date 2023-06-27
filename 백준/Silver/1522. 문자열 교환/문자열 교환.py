string = input().strip()
length = len(string)
a_cnt = string.count('a')
result = float('inf')
for i in range(length) :
  tmp = 0
  for j in range(a_cnt) :
    if string[(i + j) % length] == 'b' :
      tmp += 1
  result = min(result, tmp)
print(result)