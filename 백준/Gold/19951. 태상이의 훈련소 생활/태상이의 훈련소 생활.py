import sys
input = sys.stdin.readline

N, M = 0, 0
lands = []
changes = []

def init() :
  global lands, changes, N, M
  N, M = map(int, input().split())
  lands = list(map(int, input().split()))
  changes = [0]*(N+1)

def query() :
  for _ in range(M) :
    a, b, k = map(int, input().split())
    changes[a-1] += k
    changes[b] -= k
  for i in range(N) :
    changes[i+1] += changes[i]
    lands[i] += changes[i]
  print(*lands)

if __name__ == "__main__" :
  init()
  query()