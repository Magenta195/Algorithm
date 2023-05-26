p, m = map(int, input().split())

room_list = list()

for _ in range(p) :
  l, n = input().split()
  l = int(l)
  if not room_list :
    room_list.append([l, m == 1, [(l, n)]])
  else :
    flg = False
    for i in range(len(room_list)) :
      if not room_list[i][1] and abs(l - room_list[i][0]) <= 10 :
        room_list[i][2].append((l, n))
        flg = True
        if len(room_list[i][2]) == m :
          room_list[i][1] = True
        break
    if not flg :
      room_list.append([l, m == 1, [(l, n)]])

for _, start, _room_list in room_list :
  print('Started!' if start else 'Waiting!')
  _room_list.sort(key = lambda x : x[-1])
  for l, n in _room_list :
    print(l, n)