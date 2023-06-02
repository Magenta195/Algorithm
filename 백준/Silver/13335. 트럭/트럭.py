from collections import deque

N, W, L = map(int, input().split())
truck_list = deque(map(int, input().split()))
bridge_list = deque()
bridge_left = L
times = 0

def not_enable() :
  return bridge_left < truck or len(bridge_list) >= W or bridge_list and bridge_list[0][1] + W <= times
  
for truck in truck_list :
  times += 1
  if not_enable() :
    while not_enable() :
      _truck, start_times = bridge_list.popleft()
      times = start_times + W
      bridge_left += _truck
  bridge_left -= truck
  bridge_list.append((truck, times))

_, last = bridge_list.pop()
print(last + W)