N = int(input())
student_list = sorted(map(int, input().split()))

divisor = [0]*(student_list[-1]+1)
prev, divisor_list = 0, list()

for student in student_list :
  if prev < student :
    divisor_list = list()
    for n in range(1, int(student ** 0.5) + 1) :
      if student % n == 0 :
        divisor_list.append(n)
        if student // n != n :
          divisor_list.append(student // n)
    prev = student

  for n in divisor_list :
    divisor[n] += 1

ans = 0
for i in range(1, student_list[-1]+1) :
  if divisor[i] > 1 :
    ans = max(ans, divisor[i]*i)
print(ans)