from collections import Counter

N = int(input())
student_dict = Counter(map(int, input().split()))
maxval = max(student_dict.keys())
divisor = [0]*(maxval+1)

for key, val in student_dict.items() :
  for n in range(1, int(key ** 0.5) + 1) :
    if key % n == 0 :
      divisor[n] += val
      if key // n != n :
        divisor[key // n] += val

ans = 0
for i in range(1, maxval+1) :
  if divisor[i] > 1 :
    ans = max(ans, divisor[i]*i)
print(ans)