import sys

input = sys.stdin.readline


def is_enable_sum(array, target):
  tmp = 0
  for a in array:
    tmp += a
    if tmp > target:
      return False
    if tmp == target:
      tmp = 0

  return tmp == 0


def search(array):
  min_val, sum_val = max(array), sum(array)
  check_list = []
  for i in range(1, int(sum_val**0.5) + 1):
    if sum_val % i != 0:
      continue
    if i >= min_val:
      check_list.append(i)
    if i**2 != sum_val:
      check_list.append(sum_val // i)

  check_list.sort()
  for c in check_list:
    if is_enable_sum(array, c):
      return c
  return 0


def init():
  N = int(input())
  array = []
  cnt = N // 10
  if N % 10:
    cnt += 1
  for _ in range(cnt):
    array += list(map(int, input().split()))
  return array


def solve():
  Q = int(input())
  for _ in range(Q):
    array = init()
    print(search(array))


if __name__ == "__main__":
  solve()
