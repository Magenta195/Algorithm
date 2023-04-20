import sys

input = sys.stdin.readline
move_dict = {
  'R' : (1, 0),
  'L' : (-1, 0),
  'B' : (0, -1),
  'T' : (0, 1),
  'RT' : (1, 1),
  'LT' : (-1, 1),
  'RB' : (1, -1),
  'LB' : (-1, -1)
}


def decode_coord(x) :
  if '1' <= x <= '8' :
    return ord(x) - ord('1')
  else :
    return ord(x) - ord('A')

def encode_coord(x, y) :
  return chr(ord('A') + x) + str(y + 1)
  

def init() :
  global sx, sy, kx, ky, N
  king, stone, N = input().split()
  N = int(N)
  kx, ky = map(decode_coord, list(king))
  sx, sy = map(decode_coord, list(stone))

def move_once(mv) :
  global kx, ky, sx, sy
  mv_tuple = move_dict[mv]
  tkx, tky = kx + mv_tuple[0], ky + mv_tuple[1]
  if tkx < 0 or tkx > 7 or tky < 0 or tky > 7 :
    return

  if (tkx, tky) == (sx, sy) :
    tsx, tsy = sx + mv_tuple[0], sy + mv_tuple[1]
    if tsx < 0 or tsx > 7 or tsy < 0 or tsy > 7 :
      return
    sx, sy = tsx, tsy
  kx, ky = tkx, tky

def full_move() :
  for _ in range(N) :
    mv = input().strip()
    move_once(mv)

  print(encode_coord(kx, ky))
  print(encode_coord(sx, sy))

def solve() :
  init()
  full_move()

solve()