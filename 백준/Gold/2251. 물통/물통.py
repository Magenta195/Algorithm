from collections import defaultdict, deque

limit_list = list(map(int, input().split()))
C = limit_list[-1]
visited = defaultdict(set)
visited[C].add((0, 0))
q = deque([[0, 0, C]])
result = set([C])

while q :
  a, b, c = q.popleft()

  for i in range(3) :
    for j in range(3) :
      if i == j :
        continue
      next_list = [a, b, c]
      diff = min(limit_list[j] - next_list[j], next_list[i])
      next_list[i] -= diff
      next_list[j] += diff

      next_tuple = tuple(next_list[:2])
      if next_tuple not in visited[next_list[2]] :
        visited[next_list[2]].add(next_tuple)
        q.append(next_list)
        if not next_tuple[0] :
          result.add(next_list[2])

result = sorted(list(result))
print(*result)