from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict_dict = defaultdict(int)

for _ in range(N) :
  word = input().strip()
  if len(word) >= M :
    dict_dict[word] += 1

dict_list = list(dict_dict.keys())
dict_list.sort(key = lambda x : (-dict_dict[x], -len(x), x))

for word in dict_list :
  print(word)