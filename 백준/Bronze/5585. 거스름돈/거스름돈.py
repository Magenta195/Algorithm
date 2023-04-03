coin_list = [500, 100, 50, 10, 5]

N = 1000 - int(input())
result = 0

for coin in coin_list :
  result += N // coin
  N %= coin
  if not N :
    break

result += N
print(result)