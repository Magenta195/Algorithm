
N = int(input())
MOD = 1000000000
def matmul(a, b) :
  result = list()
  for i in range(2) :
    tmp = list()
    for j in range(2) :
      _tmp = 0
      for k in range(2) :
        _tmp = _tmp + a[i][k]*b[k][j]
      tmp.append(_tmp)
    result.append(tmp)
  return result

def matpow(mat, p) :
  if p == 1 :
    return mat

  _mat = matpow(mat, p//2)
  pmat = matmul(_mat, _mat)
  if p % 2 :
    return matmul(pmat, mat)
  else :
    return pmat

def cal_result() :
  if N == 0 :
    return (0, 0)
  if N == 1 or N == -1 :
    return (1, 1)

  if N < 0 :
    mat = [[-1, 1], [1, 0]]
    a, b, p = 0, 1, abs(N)
  else :
    mat = [[1, 1], [1, 0]]
    a, b, p = 1, 0, N-1

  mat = matpow(mat, p)
  result = a*mat[0][0] + b*mat[0][1]
  ab_result = 1 if result > 0 else (-1 if result < 0 else 0)
  return (ab_result, abs(result) % MOD)

ab_result, result = cal_result()
print(ab_result)
print(result)
