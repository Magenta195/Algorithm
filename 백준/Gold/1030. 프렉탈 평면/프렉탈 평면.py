s, N, K, R1, R2, C1, C2 = map(int, input().split())
base = [[0]*N for _ in range(N)]
for i in range((N-K)//2, (N+K)//2) :
  for j in range((N-K)//2, (N+K)//2) :
    base[i][j] = 1

def div_and_con(depth, r1, r2, c1, c2) :
  if depth == 0 :
    return [[0]]
  if depth == 1 :
    return [_base[c1:c2+1] for _base in base[r1:r2+1]]
  result = [[1]*(c2-c1+1) for _ in range(r2-r1+1)]
  block = N**(depth-1)
  for i in range(N) :
    ib = i*block
    for j in range(N) :
      jb = j*block
      if ( r1 >= ib+block or r2 < ib or
           c1 >= jb + block or c2 < jb ) :
        continue
      if (N-K) // 2 <= i < (N+K) // 2 and (N-K) // 2 <= j < (N+K) // 2 :
        continue
        
      min_r = max(ib, r1) - ib
      max_r = min(ib+block-1, r2) - ib
      min_c = max(jb, c1) - jb
      max_c = min(jb+block-1, c2) - jb
      tmp = div_and_con(depth-1, min_r, max_r, min_c, max_c)
      for _i in range(max_r-min_r+1) :
        for _j in range(max_c-min_c+1) :
          result[_i+min_r+ib-r1][_j+min_c+jb-c1] = tmp[_i][_j]
  
  return result

ans = div_and_con(s, R1, R2, C1, C2)
for _ans in ans :
  print(*_ans, sep='')