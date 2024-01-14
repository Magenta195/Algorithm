N = int(input())
ans = sorted(range(1, N+1), key = lambda x : (x % 2, x))
lans, rans = ans[:N//2], ans[N//2:]
if N % 6 == 3 :
  lans.append(lans.pop(0))
  rans.append(rans.pop(0))
  rans.append(rans.pop(0))
  print(*(lans+rans), sep = '\n')
elif N % 6 == 2 :
  rans[0], rans[1] = rans[1], rans[0]
  del rans[2]
  print(*(lans+rans+[5]), sep = '\n')
else :
  print(*ans, sep = '\n')