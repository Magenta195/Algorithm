from itertools import combinations
import sys
input = sys.stdin.readline
check_set = set(['a', 'e', 'i', 'o', 'u'])

L, C = map(int,input().split())
alphabet_list = list(input().split())
answer = list()

for word_list in combinations(alphabet_list, L) :
  consonant = 0
  vowel = 0
  for w in word_list :
    if w in check_set :
      vowel += 1
    else :
      consonant += 1
  if vowel and consonant >= 2 :
    answer.append(''.join(sorted(word_list)))

for word in sorted(answer) :
  print(word)