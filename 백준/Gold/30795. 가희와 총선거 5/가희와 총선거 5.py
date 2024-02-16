def convert(string, score_dict) :
  mod = 0
  character, group, team = [], '', ''
  idx = 0
  result = list()
  for s in string.split() :
    if s == 'Group' :
      mod = 1
    elif s == 'Team' :
      mod = 2
    else :
      if mod == 0 :
        character.append(s)
      elif mod == 1 :
        group = s
      else :
        team = s
        score_dict[(group, team, ' '.join(character))] = (idx+1, idx // 16+1)
        character, group, team = [], '', ''
        mod = 0
        idx += 1

before = input().strip()
after = input().strip()
before_dict = dict()
after_dict = dict()
convert(before, before_dict)
convert(after, after_dict)

keys = set(before_dict.keys()).union(set(after_dict.keys()))
for key in keys :
  if key not in before_dict :
    before_dict[key] = (81, 6)
  if key not in after_dict :
    after_dict[key] = (81, 6)
    
score_dict = dict()
for key in keys :
  bi, btier = before_dict[key]
  ai, atier = after_dict[key]
  if atier == 6 :
    score_dict[key] = 0
    continue
  score = 0
  cond_1 = False
  if btier > atier :
    score += 10000*(btier - atier)
    cond_1 = True
  if (ai - 1) % 16 == 0 :
    score += 20000 if cond_1 else 10000
  if btier != 1 and atier == 1 :
    p = 0
    for _key in keys :
      if before_dict[key] <= before_dict[_key] :
        continue
      if after_dict[key] >= after_dict[_key] :
        continue
      if before_dict[_key][1] == 1 and after_dict[_key][1] != 1 :
        p += 1
    score += 30000*p
  score_dict[key] = score

result = sorted(score_dict.keys(), key = lambda x : (-score_dict[x], after_dict[x]))
print(*result[0], sep = '\n')