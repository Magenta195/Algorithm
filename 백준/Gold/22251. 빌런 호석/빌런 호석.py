num_dict = {
  '0' : int('1111110', 2),
  '1' : int('0110000', 2),
  '2' : int('1101101', 2),
  '3' : int('1111001', 2),
  '4' : int('0110011', 2),
  '5' : int('1011011', 2),
  '6' : int('1011111', 2),
  '7' : int('1110000', 2),
  '8' : int('1111111', 2),
  '9' : int('1111011', 2)
}

N, K, P, X = map(int, input().split())
X = list(str(X).rjust(K, '0'))

def dfs(num_list, idx, changed) :
  if idx == K :
    return 1 if changed and 1 <= int(''.join(num_list)) <= N else 0

  next_num_list = num_list[:]
  num = num_list[idx]
  result = 0
  for i in range(10) :
    next_num_list[idx] = str(i)
    next_changed = bin(num_dict[str(i)] ^ num_dict[num]).count('1') + changed
    next_num = int(''.join(next_num_list))
    if next_changed <= P :
      result += dfs(next_num_list, idx+1, next_changed)

  return result

print(dfs(X, 0, 0))    