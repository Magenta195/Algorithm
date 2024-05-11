import sys
from heapq import heappush, heappop

input = sys.stdin.readline

visit_dict = {}
min_heap = []
max_heap = []


def init():
  N = int(input())
  for _ in range(N):
    P, L = map(int, input().split())
    visit_dict[P] = L
    heappush(min_heap, (L, P))
    heappush(max_heap, (-L, -P))


def validate(mode):
  if mode:
    while -max_heap[0][1] not in visit_dict or -max_heap[0][0] != visit_dict[-max_heap[0][1]]:
      heappop(max_heap)
  else:
    while min_heap[0][1] not in visit_dict or min_heap[0][0] != visit_dict[min_heap[0][1]]:
      heappop(min_heap)


def query():
  Q = int(input())
  for _ in range(Q):
    q, *cmd = input().split()
    if q == "add":
      P, L = map(int, cmd)
      visit_dict[P] = L
      heappush(min_heap, (L, P))
      heappush(max_heap, (-L, -P))
    elif q == "recommend":
      if cmd[0] == "1":
        validate(True)
        print(-max_heap[0][1])
      else:
        validate(False)
        print(min_heap[0][1])
    else:
      P = int(cmd[0])
      del visit_dict[P]


if __name__ == "__main__":
  init()
  query()
