import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi_list = [int(input()) for _ in range(N)]
sushi_seq = sushi_list[:k]
result = 0
for i in range(N) :
  sushi_seq.pop(0)
  sushi_seq.append(sushi_list[(i + k) % N])
  result = max(result, len(set(sushi_seq + [c])))
  if result == d :
    break
print(result)