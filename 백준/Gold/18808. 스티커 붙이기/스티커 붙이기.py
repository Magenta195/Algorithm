import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
map_list = [[0]*M for _ in range(N)]
answer = 0

def rotate(sticker) :
  result = list()
  for x, y in sticker :
    result.append((-y, x))
  return result

def patch(sticker) :
  for i in range(N) :
    for j in range(M) :
      cnt = 0
      for x, y in sticker :
        ax, ay = x + j, y + i
        if not (-1 < ax < M and -1 < ay < N and map_list[ay][ax] == 0) :
          break
        cnt += 1
      if cnt == len(sticker) :
        for x, y in sticker :
          ax, ay = x + j, y + i
          map_list[ay][ax] = 1
        return True
  return False

def patch_and_rotate(sticker) :
  global answer
  for _ in range(4) :
    if not patch(sticker) :
      sticker = rotate(sticker)
    else :
      answer += len(sticker)
      return
  return

for _ in range(K) :
  R, C = map(int, input().split())
  sticker_map = [list(map(int, input().split())) for i in range(R)]
  sticker_list = list()
  for i in range(R) :
    for j in range(C) :
      if sticker_map[i][j] == 1 :
        sticker_list.append((j, i))
  patch_and_rotate(sticker_list)

print(answer)