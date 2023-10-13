def gcd(a, b) :
  while b :
    a, b = b, a % b
  return a

def lcm(a, b) :
  return a // gcd(a,b) * b

N = int(input())
adj_list = [list() for _ in range(N)]
ingredient_list = [[(-1, -1)]*N for _ in range(N)]

for _ in range(N-1) :
  a, b, p, q = map(int, input().split())
  pq_gcd = gcd(p, q)
  p //= pq_gcd
  q //= pq_gcd
  ingredient_list[a][b] = (p, q)
  ingredient_list[b][a] = (q, p) 
  
for k in range(N) :
  for i in range(N) :
    for j in range(N) :
      if ingredient_list[i][j] != (-1, -1) or i == j:
        continue
      if ingredient_list[i][k] != (-1, -1) and ingredient_list[k][j] != (-1, -1) :
        p, q1 = ingredient_list[i][k]
        q2, r = ingredient_list[k][j]
        q_lcm = lcm(q1, q2)
        p *= q_lcm // q1
        r *= q_lcm // q2
        ingredient_list[i][j] = (p, r)

answer = [1]*N
for i in range(1, N) :
  answer[0] *= ingredient_list[0][i][0]

all_gcd = answer[0]
for i in range(1, N) :
  answer[i] = answer[0] // ingredient_list[0][i][0] * ingredient_list[0][i][1]
  all_gcd = gcd(all_gcd, answer[i])

for i in range(N) :
  answer[i] //= all_gcd

print(*answer)