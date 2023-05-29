import sys
input = sys.stdin.readline

N, X = map(int, input().split())
_num_list = list(map(int,input().split()))
num_list = [ sum(_num_list[:X]) ]

for num1, num2 in zip(_num_list[:N-X], _num_list[X:]) :
  num_list.append(num_list[-1] - num1 + num2)

result = max(num_list)
if result :
  print(result)
  print(num_list.count(result))
else :
  print('SAD')