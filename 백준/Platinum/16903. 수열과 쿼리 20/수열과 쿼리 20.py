import sys
input = sys.stdin.readline

MAX = 29
trie = {}

def add(num) :
  cur = trie
  for i in range(MAX, -1, -1) :
    tar = 1 if num & (1 << i) else 0
    if tar not in cur :
      cur[tar] = { 2 : 1 }
    else :
      cur[tar][2] += 1
    cur = cur[tar]

def delete(num) :
  cur = trie
  for i in range(MAX, -1, -1) :
    tar = 1 if num & (1 << i) else 0
    cur[tar][2] -= 1
    if not cur[tar][2] :
      del cur[tar]
      return
    cur = cur[tar]

def search(num) :
  cur = trie
  res = 0
  for i in range(MAX, -1, -1) :
    flg = num & (1 << i)
    _range = [0, 1] if num & (1 << i) else [1, 0]
    for j in _range :
      if j in cur :    
        break
    if j and not flg or not j and flg :
      res += 1 << i
    cur = cur[j]
  print(res)

M = int(input())
add(0)
for _ in range(M) :
  q, x = map(int, input().split())
  if q == 1 :
    add(x)
  elif q == 2 :
    delete(x)
  else :
    search(x)