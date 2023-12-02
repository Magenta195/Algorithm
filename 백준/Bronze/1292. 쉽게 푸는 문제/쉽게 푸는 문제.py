a, b = map(int, input().split())
num_list = list()
for i in range(1, 101) :
    num_list += [i]*i

print(sum(num_list[a-1:b]))