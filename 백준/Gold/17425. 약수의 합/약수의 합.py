import sys
input = sys.stdin.readline

max = 10 ** 6
fval = [1] * (max + 1)
gval = [0]

def init() :
  for i in range(2, max+1) :
    for j in range(i, max+1, i) :
      fval[j] += i

  for i in range(1, max+1) :
    gval.append(gval[-1] + fval[i])

def query() :
  Q = int(input())
  for _ in range(Q) :
    print(gval[int(input())])

if __name__ == "__main__" :
  init()
  query()