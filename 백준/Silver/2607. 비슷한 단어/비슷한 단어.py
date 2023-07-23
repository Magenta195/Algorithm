from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

def make_dict(word) :
  length = len(word)
  result = defaultdict(int)
  for s in word :
    result[s] += 1
  return result, length

def compare_dict(target) :
  global word_dict, str_set
  diff = 0
  union_set = str_set.union(set(target.keys()))
  for s in union_set :
    diff += abs(word_dict[s] - target[s])
  return diff

answer = 0
word_dict, word_len = make_dict(input().strip())
str_set = set(word_dict.keys())
for _ in range(N-1) :
  target_dict, target_len = make_dict(input().strip())
  diff = compare_dict(target_dict)
  if (diff == 2 or diff == 0) and word_len == target_len :
    answer += 1
  elif diff == 1 and abs(word_len - target_len) == 1 :
    answer += 1

print(answer)

  