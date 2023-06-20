N, M = map(int, input().split())
book_list = list(map(int, input().split()))
pos_sector, neg_sector = [0], [0]
for num in book_list :
  if num > 0 :
    pos_sector.append(num)
  else :
    neg_sector.append(-num)

pos_sector.sort()
neg_sector.sort()
max_val = max(pos_sector[-1], neg_sector[-1])
result = 0

while pos_sector :
  result += pos_sector[-1] * 2
  cnt = 0
  while pos_sector and cnt < M :
    cnt += 1
    pos_sector.pop()

while neg_sector :
  result += neg_sector[-1] * 2
  cnt = 0
  while neg_sector and cnt < M :
    cnt += 1
    neg_sector.pop()

print(result - max_val)