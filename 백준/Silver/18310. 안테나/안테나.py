import sys
N = int(input())
num_list = sorted(list(map(int, input().split())))
print(num_list[(N-1)//2])