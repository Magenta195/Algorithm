from itertools import combinations, permutations

word_list = [input().strip() for _ in range(6)]

def transpose(lst) :
  result = ['']*3 
  for i in range(3) :
    for j in range(3) :
      result[j] += lst[i][j] 
  return result
      
answer = 'zzzzzzzzz'
for num_list in combinations(range(6), 3) :
  other_nums = set(range(6)) - set(num_list)
  words = [ word_list[i] for i in num_list ]
  other_words = list( word_list[i] for i in other_nums )
  other_words.sort()

  for orders in permutations(range(3), 3) :
    t_words = [ words[i] for i in orders ]
    target_words = transpose(t_words)
    target_words.sort()
    if target_words == other_words :
      t_words = ''.join(t_words)
      if answer > t_words :
        answer = t_words

if answer != 'zzzzzzzzz' :
  for i in range(3) :
    print(answer[i*3:i*3+3])
else :
  print(0)
    