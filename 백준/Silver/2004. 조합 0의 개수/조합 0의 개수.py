n, m = map(int, input().split())

def cal_twos_fives(num) :
  twos, fives = 0, 0
  n = 2
  while n <= num :
    twos += num // n
    n *= 2
  n = 5
  while n <= num :
    fives += num // n
    n *= 5
  return twos, fives

twos, fives = cal_twos_fives(n)
for num in [n-m, m] :
  stwos, sfives = cal_twos_fives(num)
  twos -= stwos
  fives -= sfives

print(min(twos, fives))