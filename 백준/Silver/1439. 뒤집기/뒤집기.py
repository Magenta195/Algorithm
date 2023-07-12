string = input().strip()
count_dict = { '0' : 0, '1' : 0 }
cur = string[0]
count_dict[cur] += 1

for s in string[1:] :
  if cur != s :
    count_dict[s] += 1
    cur = s
print(min(count_dict.values()))