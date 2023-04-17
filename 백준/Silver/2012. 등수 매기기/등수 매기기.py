import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort()
answer = 0

for i in range(N) :
  answer += abs(i+1 - num_list[i])

print(answer)