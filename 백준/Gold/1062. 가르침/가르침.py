from itertools import combinations

spell_set = set(['a', 't', 'n', 'i', 'c'])

def init() :
  N, K = map(int, input().split())
  word_list = list()
  full_spell_set = set()
  for _ in range(N) :
    words = set(input().strip()) - spell_set
    word_list.append(words)
    full_spell_set |= words
  K -= 5

  return N, K, word_list, full_spell_set

def spell_check(spell_set, word_list) :
  result = 0
  for word in word_list :
    if not word - spell_set :
      result += 1
  return result

def full_spell_check(K, full_spell_set, word_list) :
  result = 0
  for comb in map(set, combinations(full_spell_set, K)) :
    result = max(result, spell_check(comb, word_list))

  return result

def solve() :
  N, K, word_list, full_spell_set = init()
  if K < 0 :
    print(0)
    return
  if K >= len(full_spell_set) :
    print(N)
    return

  result = full_spell_check(K, full_spell_set, word_list)
  print(result)

solve()