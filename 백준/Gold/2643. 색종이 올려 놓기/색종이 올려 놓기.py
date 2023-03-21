N = int(input())

def init() :
  paper_list = list()
  for _ in range(N) :
    h, w = map(int, input().split())
    if h < w :
      h, w = w, h
    paper_list.append((h, w))
    
  paper_list.sort(reverse = True)
  return paper_list

def make_dp(paper_list) :
  dp = [1]*N

  for i in range(N-1) :
    ih, iw = paper_list[i]
    for j in range(i+1, N) :
      jh, jw = paper_list[j]
      if ih >= jh and iw >= jw :
        dp[j] = max(dp[j], dp[i] + 1)

  print(max(dp))
  
def solve() :
  paper_list = init()
  make_dp(paper_list)

solve()
