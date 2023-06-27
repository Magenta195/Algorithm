from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
  N = int(input())
  num_list = list(map(int, input().split()))
  num_cnt = defaultdict(int)
  num_dict = defaultdict(list)

  for num in num_list :
    num_cnt[num] += 1
  num_list = [ x for x in num_list if num_cnt[x] == 6 ]
  for idx, num in enumerate(num_list) :
    num_dict[num].append(idx)
  result = list(num_dict.keys())
  result.sort( key = lambda x : (sum(num_dict[x][:4]), num_dict[x][4], num_dict[x][5]))
  print(result[0])