from heapq import *
import sys
input = sys.stdin.readline

def init() :
  n = int(input())
  line_list = list()
  
  for _ in range(n) :
    h, o = map(int, input().split())
    if h > o :
      h, o = o, h
    line_list.append((h, o))

  line_list.sort(key = lambda x : (x[1], x[0]))
  d = int(input())

  return line_list, d

def traversal(line_list, d) :
  q = []
  result = 0
  
  for h, o in line_list :
    if o - h > d :
      continue
    heappush(q, (h, o))
    while o - q[0][0] > d :
      heappop(q)
    
    result = max(result, len(q))

  return result

def solve() :
  line_list, d = init()
  result = traversal(line_list, d)
  print(result)

solve()