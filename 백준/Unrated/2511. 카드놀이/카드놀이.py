a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_score, b_score = 0, 0
is_a_win = True
for a, b in zip(a_list, b_list) :
  if a > b :
    a_score += 3
    is_a_win = True
  elif a < b :
    b_score += 3
    is_a_win = False
  else :
    a_score += 1
    b_score += 1

print(a_score, b_score)
if a_score > b_score or a_score == b_score != 10 and is_a_win:
  print("A")
elif a_score < b_score or a_score == b_score != 10 and not is_a_win:
  print("B")
else :
  print("D")