import sys

n = int(sys.stdin.readline())
lst = [[x for x in map(int, sys.stdin.readline().split())] for _ in range(n)]
lst.sort(key = lambda x:(x[0], x[1]))

for l in lst:
    print(*l)