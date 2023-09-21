from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = float('inf')
sentence = input().strip()
N = int(input())
word_list = [list() for _ in range(51)]

for i in range(N) :
  word = input().strip()
  word_list[len(word)].append(word)

def word_distance(source, target) :
  dist = 0

  source_dict = defaultdict(int)
  target_dict = defaultdict(int)
  for i in range(len(source)) :
    source_dict[source[i]] += 1
    target_dict[target[i]] += 1
    if source[i] != target[i] :
      dist += 1

  for key in source_dict.keys() :
    if source_dict[key] != target_dict[key] :
      return -1

  return dist

dp = [MAX]*(len(sentence)+1)
dp[0] = 0

for i in range(len(sentence)) :
  if dp[i] == MAX : 
    continue
  target = sentence[i]
  for j in range(1, 51) :
    if i+j > len(sentence) :
      break
    for word in word_list[j] :
      dist = word_distance(word, target)
      if dist == -1 :
        continue
      dp[i+j] = min(dp[i+j], dp[i] + dist)
    if i+j < len(sentence) :
      target += sentence[i+j]

print(dp[-1] if dp[-1] < MAX else -1)