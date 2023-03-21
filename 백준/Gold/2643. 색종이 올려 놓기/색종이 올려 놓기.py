N = int(input())

def init() :
  paper_list = [list(map(int, input().split())) for _ in range(N)]
  paper_list.sort(key = lambda x : -x[0]*x[1])
  return paper_list

def make_dp(paper_list) :
  dp = [1]*N

  for i in range(N-1) :
    ih, iw = paper_list[i]
    for j in range(i+1, N) :
      jh, jw = paper_list[j]
      if ih >= jh and iw >= jw or ih >= jw and iw >= jh :
        dp[j] = max(dp[j], dp[i] + 1)

  print(max(dp))
  
def solve() :
  paper_list = init()
  make_dp(paper_list)

solve()
