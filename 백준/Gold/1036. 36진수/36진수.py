from collections import defaultdict

N = int(input())
num_dict = defaultdict(int)
sum_val = 0
for i in range(N) :
  num = input().strip()
  length = len(num)
  for i in range(length) :
    if num[i].isdigit() :
      exp_val = (35 - int(num[i])) * 36 ** (length - i - 1)
      sum_val += int(num[i]) * 36 ** (length - i - 1)
    else :
      exp_val = (25 - ord(num[i]) + ord('A')) * (36 ** (length - i - 1))
      sum_val += (ord(num[i]) - ord('A') + 10) * 36 ** (length - i - 1)
    num_dict[num[i]] += exp_val
K = int(input())
num_list = sorted(num_dict.values(), reverse = True)
for i in range(min(K, len(num_list))) :
  sum_val += num_list[i]
  
answer = ''
while sum_val :
  num = sum_val % 36
  if num >= 10 :
    num = chr(num + 55)
  answer = str(num) + answer
  sum_val //= 36

print(answer if answer else '0')