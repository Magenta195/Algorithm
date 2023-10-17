N = int(input())
M = int(N**0.5)
is_prime_num = [True for _ in range(N+1)]
is_prime_num[0] = is_prime_num[1] = False
for i in range(2, M+1) :
  if is_prime_num[i] :
    for j in range(i*2, N+1, i) : 
      is_prime_num[j] = False

prime_num = list()
for i in range(2, N+1) :
  if is_prime_num[i] :
    prime_num.append(i)

w = len(prime_num)
for i in range(w) :
  for j in range(i, w) :
    for k in range(j, w) :
      if prime_num[i] + prime_num[j] + prime_num[k] < N and is_prime_num[N - prime_num[i] - prime_num[j] - prime_num[k]] :
          print(prime_num[i], prime_num[j], prime_num[k], N - prime_num[i] - prime_num[j] - prime_num[k])
          exit()
print(-1)