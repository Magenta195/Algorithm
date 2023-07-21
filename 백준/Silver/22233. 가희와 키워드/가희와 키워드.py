import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = set([input().strip() for _ in range(N)])

for _ in range(M) :
  key_set = set(input().strip().split(','))
  keywords -= key_set
  print(len(keywords))