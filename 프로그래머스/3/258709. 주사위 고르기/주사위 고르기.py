from itertools import combinations, product

def lower_bound(lst, target) :
    start, end = 0, len(lst)
    while start < end :
        mid = (start + end) // 2
        if lst[mid] < target :
            start = mid + 1
        else :
            end = mid
    return end


def roll(a_dice, b_dice):
    length = len(a_dice)
    a_res = []
    b_res = []
    for perm in product(range(6), repeat = length) :
        a_res.append(sum([a_dice[i][perm[i]] for i in range(length)]))
        b_res.append(sum([b_dice[i][perm[i]] for i in range(length)]))
    
    b_res.sort()
    res = 0
    for a in a_res :
        res += lower_bound(b_res, a)
    return res

def solution(dice):
    length = len(dice)
    max_win, ans = 0, []
    for comb in combinations(range(length), length // 2) :
        b_comb = [x for x in range(length) if x not in comb]
        a_dice = [dice[x] for x in comb]
        b_dice = [dice[x] for x in b_comb]
        res = roll(a_dice, b_dice)
        if res > max_win :
            max_win, ans = res, sorted(map(lambda x : x + 1, comb))
    
    return ans