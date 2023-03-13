n=int(input())
s=[[1,0],[0,1]]
for i in range(2,41):s.append([s[i-2][0]+s[i-1][0],s[i-2][1]+s[i-1][1]])
for _ in range(n):
    i=int(input())
    print(s[i][0],s[i][1])