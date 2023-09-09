N = int(input())
num_list = list(map(int, input().split()))
if N == 1 :
  print("A")
elif N == 2 :
  print("A" if num_list[0] != num_list[1] else num_list[0])
else :
  if num_list[1] == num_list[0] :
    if num_list[2] != num_list[1] :
      print("B")
      exit()
    a, b = 1, 0
  else :
    a = (num_list[2] - num_list[1]) / (num_list[1] - num_list[0])
    if not a.is_integer() :
      print("B")
      exit()
    a = int(a)
    b = num_list[1] - num_list[0] * a
  for i in range(1, N) :
    if num_list[i-1] * a + b != num_list[i] :
      print("B")
      exit()
  print(num_list[-1] * a + b)