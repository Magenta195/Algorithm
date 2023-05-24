import sys
input = sys.stdin.readline

def make_postorder(preorder, inorder) :
  if not preorder :
    return list()
  root = preorder[0]
  idx = inorder.index(root)
  left = make_postorder(preorder[1:idx+1], inorder[:idx])
  right = make_postorder(preorder[idx+1:], inorder[idx+1:])
  return left + right + [root]

for _ in range(int(input())) :
  n = int(input())
  preorder = list(map(int, input().split()))
  inorder = list(map(int, input().split()))
  result = make_postorder(preorder, inorder)
  print(*result)