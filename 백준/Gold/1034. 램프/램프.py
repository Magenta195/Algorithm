from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_dict = [ defaultdict(int) for _ in range(m+1) ]
for _ in range(n) :
  string = input().strip()
  num_dict[string.count('0')][string] += 1

k = int(input())
ans = 0
for i in range(k%2, min(m+1, k+1), 2) :
  for val in num_dict[i].values() :
    ans = max(ans, val)
print(ans)
