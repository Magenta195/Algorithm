# 어드벤쳐게임
'''https://www.acmicpc.net/problem/2310'''

import sys

try:
    while True:
        n = int(sys.stdin.readline())
        if not n:
            break
        graph = dict()
        dp_arr = [-1] * (n+1)
        alpha_cost = [None]

        for i in range(1,n+1):
            input_list = sys.stdin.readline().split(' ')
            alpha_cost.append((input_list[0], int(input_list[1])))
            graph[i] = list(map(int, input_list[2:-1]))

        k = 0
        dp_arr[1] = alpha_cost[1][1]
        
        # print(graph)

        for i in range(1, n+1):
            for room_ in graph[i]:
                alpha_, cost_ = alpha_cost[room_]
                if alpha_ == 'E':
                    dp_arr[room_] = max(dp_arr[room_], dp_arr[i])
                elif alpha_ == 'L':
                    dp_arr[room_] = max(dp_arr[room_], dp_arr[i], cost_)
                else:
                    dp_arr[room_] = max(dp_arr[room_], dp_arr[i] - cost_)

                if room_ == n and dp_arr[room_] >= 0:
                    k = 1
                    break
            if k:
                break
        
        if dp_arr[n] >= 0:
            print('Yes')
        else:
            print('No')



except ValueError or IndexError as e:
    print(e)