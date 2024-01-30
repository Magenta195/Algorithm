import sys
input = sys.stdin.readline

word_dict = ['A', 'E', 'I', 'O', 'U']
word_dict = { key : val for val, key in enumerate(word_dict)}

N = int(input())
word_list = [input().strip() for _ in range(N)]
dp = [[[0]*5 for _ in range(5)] for _ in range(1 << N)]
ans = 0

for i in range(N) :
  word = word_list[i]
  start, end = word_dict[word[0]], word_dict[word[-1]]
  dp[1 << i][start][end] = len(word)
  ans = max(ans, len(word))

for i in range(1, 1 << N) :
  for j in range(5) :
    for k in range(5) :
      if not dp[i][j][k] :
        continue
      for l in range(N) :
        if i & (1 << l) :
          continue
        word = word_list[l]
        start, end = word_dict[word[0]], word_dict[word[-1]]
        if k != start :
          continue
        dp[i | (1 << l)][j][end] = dp[i][j][k] + len(word)
        ans = max(ans, dp[i | (1 << l)][j][end])
print(ans)