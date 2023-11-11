from collections import defaultdict

N = int(input())
alphabet_dict = defaultdict(int)

for _ in range(N) :
  string = input().strip()
  length = len(string)
  for i in range(length) :
    alphabet_dict[string[i]] += 10 ** (length - i - 1)

ans = 0
num = 9
for key in sorted(alphabet_dict.keys(), key = lambda x : -alphabet_dict[x]) :
  ans += alphabet_dict[key] * num
  num -= 1
print(ans)