N = int(input())
A_list = list(sorted(map(int, input().split())))
B_list = list(sorted(map(int, input().split()), reverse = True))
answer = 0

for i in range(N) :
  for j in range(N) :
    if A_list[i] > B_list[j] != 0 :
      A_list[i] = B_list[j] = 0
      answer += 2
      break
for i in range(N) :
  if not A_list[i] :
    continue
  for j in range(N) :
    if A_list[i] == B_list[j] != 0 :
      B_list[j] = 0
      answer += 1
      break
      
print(answer)