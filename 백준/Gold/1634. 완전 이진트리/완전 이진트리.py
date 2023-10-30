k = int(input())
T1 = list(map(int, input().split()))
T2 = list(map(int, input().split()))

def div_and_con(depth, start, end, left, right) :
  if depth == k :
    return 1 if T1[left] == T2[start] else 0

  mid = (start + end) // 2
  center = (left + right) // 2
  orig_result = div_and_con(depth+1, start, mid, left, center) + div_and_con(depth+1, mid+1, end, center+1, right)
  rev_result = div_and_con(depth+1, mid+1, end, left, center) + div_and_con(depth+1, start, mid, center+1, right)

  return max(orig_result, rev_result)

print(div_and_con(1, 0, 2**(k-1)-1, 0, 2**(k-1)-1))