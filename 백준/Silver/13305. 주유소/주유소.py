N = int(input())
road_cost = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))
answer = 0

prev = oil_cost[0]
for i in range(N-1) :
  answer += prev * road_cost[i]
  if prev > oil_cost[i+1] :
    prev = oil_cost[i+1]
print(answer)