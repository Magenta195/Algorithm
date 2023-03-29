from collections import deque
import sys
input = sys.stdin.readline

def init() :
  global N, C, M
  N, C = map(int, input().split())
  M = int(input())

  post_list = [list(map(int, input().split())) for _ in range(M)]
  post_list.sort(key = lambda x : (x[1], x[0]))
  return post_list

def greedy_search(post_list) :
  global C
  left = C
  post_queue = deque()
  result = 0

  for start, end, box in post_list :
    while post_queue and post_queue[0][0] <= start :
      _, _box = post_queue.popleft()
      left += _box

    if left > 0 :
      enable_box = min(box, left)
      post_queue.append((end, enable_box))
      left -= enable_box
      result += enable_box

  return result

def solve() :
  post_list = init()
  result = greedy_search(post_list)

  print(result)

solve()  