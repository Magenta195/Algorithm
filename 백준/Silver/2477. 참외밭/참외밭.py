K = int(input())

tot_list = list()
w_max = 0
h_max = 0

for _ in range(6) :
  d, n = map(int, input().split())
  tot_list.append(n)
  if d >= 3 :
    w_max = max(w_max, n)
  else :
    h_max = max(h_max, n)

w_idx = tot_list.index(w_max)
h_idx = tot_list.index(h_max)

w_min = w_max - min(tot_list[(h_idx+1)%6], tot_list[(h_idx-1)%6])
h_min = h_max - min(tot_list[(w_idx+1)%6], tot_list[(w_idx-1)%6])

print(K*(w_max*h_max - w_min*h_min))