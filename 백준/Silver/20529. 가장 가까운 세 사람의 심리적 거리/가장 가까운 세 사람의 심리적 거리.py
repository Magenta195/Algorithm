import sys
input = sys.stdin.readline

def dist(a, b, c) :
  result = 0
  for i in range(4) :
    if a[i] != b[i] :
      result += 1
    if b[i] != c[i] :
      result += 1
    if c[i] != a[i] :
      result += 1
  return result

T = int(input())
for _ in range(T) :
  N = int(input())
  mbti = input().split()
  if N > 32 :
    print(0)
    continue
  answer = float('inf')
  for i in range(N-2) :
    for j in range(i+1, N-1) :
      for k in range(j+1, N) :
        tmp = dist(mbti[i], mbti[j], mbti[k])
        if tmp < answer :
          answer = tmp
  print(answer)