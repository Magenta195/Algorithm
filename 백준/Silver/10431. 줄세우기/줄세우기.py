import sys
input = sys.stdin.readline

def solve() :
  N, *student_list = map(int, input().split())
  result = 0
  sorted_list = list()

  for i in range(20) :
    flg = False
    for j in range(i) :
      if sorted_list[j] > student_list[i] :
        sorted_list = sorted_list[:j] + [student_list[i]] + sorted_list[j:]
        result += i-j
        flg = True
        break
    if not flg :
      sorted_list.append(student_list[i])

  print(N, result)

for _ in range(int(input())) :
  solve()