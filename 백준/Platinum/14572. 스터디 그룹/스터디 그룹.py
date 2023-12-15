from collections import defaultdict
import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
algo_dict = defaultdict(int)
student_list = list()

for _ in range(N) :
  M, d = map(int, input().split())
  student_list.append([d] + list(map(int, input().split())))

student_list.sort()
ans = 0
l, r = 0, 0
while r < N :
  for algo in student_list[r][1:] :
    algo_dict[algo] += 1
  r += 1
  while l < r and student_list[r-1][0] - student_list[l][0] > D :
    for algo in student_list[l][1:] :
      algo_dict[algo] -= 1
      if not algo_dict[algo] :
        del algo_dict[algo]
    l += 1
  algo_len = len(algo_dict.keys())
  E = (algo_len - list(algo_dict.values()).count(r-l)) * (r - l)
  ans = max(ans, E)

print(ans)