from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
leaf_dict = {}
level_list = [-1]*N
is_root = [True]*N

for _ in range(N) :
  node, left, right = map(int, input().split())
  if left > -1 :
    is_root[left-1] = False
  if right > -1 :
    is_root[right-1] = False
  leaf_dict[node-1] = (left-1, right-1)

def tree_search(node, level) :
  level_list[node] = level
  left, right = leaf_dict[node]
  left_subtree, right_subtree = list(), list()
  if left > -1 :
    left_subtree = tree_search(left, level+1)
  if right > -1 :
    right_subtree = tree_search(right, level+1)

  return left_subtree + [node] + right_subtree

for i in range(N) :
  if is_root[i] :
    tree_list = tree_search(i, 0)
    break

answer_dict = {}
for i, node in enumerate(tree_list) :
  if level_list[node] not in answer_dict :
    answer_dict[level_list[node]] = [i, i]
    continue
  answer_dict[level_list[node]][-1] = i

answer_level, answer_width = -1, -1
for level, (minval, maxval) in sorted(answer_dict.items()) :
  if maxval - minval + 1 > answer_width :
    answer_level, answer_width = level+1, maxval - minval + 1

print(answer_level, answer_width)