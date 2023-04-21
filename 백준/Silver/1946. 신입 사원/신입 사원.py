import sys
input = sys.stdin.readline

def init() :
  global N, score_list
  N = int(input())
  score_list = [list(map(int, input().split())) for _ in range(N)]

def sort_and_count() :
  score_list.sort(key = lambda x : (x[0], -x[1]) )
  cnt = 0
  prev_s1, prev_s2 = float('inf'), float('inf')
  for s1, s2 in score_list :
    if s1 > prev_s1 and s2 > prev_s2 :
      continue
    cnt += 1
    prev_s1, prev_s2 = s1, s2

  print(cnt)

def solve() :
  for _ in range(int(input())) :
    init()
    sort_and_count()

solve()
