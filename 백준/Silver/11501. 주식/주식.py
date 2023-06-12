import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
  N = int(input())
  price_list = list(map(int, input().split()))
  result = 0
  max_price = price_list[-1]
  for i in range(N-2, -1, -1) :
    if price_list[i] <= max_price :
      result += max_price - price_list[i]
    else :
      max_price = price_list[i]
  print(result)