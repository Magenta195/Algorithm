from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def solve() :
  M = int(input())
  num_list = list()
  for i in range((M-1) // 10 + 1) :
    num_list += list(map(int, input().split()))
  left_q, right_q, answer = list(), list(), list()
  left_q.append(-num_list[0])
  answer.append(num_list[0])
  
  for i in range(1, M) :
    if -left_q[0] < num_list[i] :
      heappush(right_q, num_list[i])
    else :
      heappush(left_q, -num_list[i])

    while len(left_q) - len(right_q) > 1 :
      heappush(right_q, -heappop(left_q))
    while len(left_q) - len(right_q) < 0 :
      heappush(left_q, -heappop(right_q))
    if not i % 2 :
      answer.append(-left_q[0])

  print(len(answer))
  for i in range(0, len(answer), 10) :
    print(*answer[i:min(i+10, len(answer))])

for _ in range(int(input())) :
  solve()