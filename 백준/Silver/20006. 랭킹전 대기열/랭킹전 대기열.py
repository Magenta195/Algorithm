p, m = map(int, input().split())
room_list = list()

for _ in range(p) :
  l, n = input().split()
  l = int(l)
  flg = False
  for i in range(len(room_list)) :
    if len(room_list[i]) < m and abs(l - room_list[i][0][0]) <= 10 :
      room_list[i].append((l, n))
      flg = True
      break
  if not flg :
    room_list.append([(l, n)])

for _room_list in room_list :
  print('Started!' if len(_room_list) == m else 'Waiting!')
  _room_list.sort(key = lambda x : x[-1])
  for l, n in _room_list :
    print(l, n)