import sys
input = sys.stdin.readline

def solve() :
  N, M = map(int, input().split())
  book_needs = [list(map(int, input().split())) for _ in range(M)]
  book_needs.sort(key = lambda x : (x[1], x[0]))
  answer = 0
  
  book_visited = [False]*(N+1)
  for a, b in book_needs :
    for i in range(a, b+1) :
      if not book_visited[i] :
        book_visited[i] = True
        answer += 1
        break
  print(answer)

T = int(input())
for _ in range(T) :
  solve()