import sys
sys.setrecursionlimit(10**6)

N = int(input())
MOD = 9901
def roundup(num) :
  return int(num) + 1 if (num - int(num)) >= 0.5 else int(num)

def hanoi(num) :
  if num == 1 :
    return 1
  K = num + 1 - roundup((2*num + 1) ** 0.5)
  return (2*hanoi(K) + 2 ** (num - K) - 1) % MOD
print(hanoi(N))