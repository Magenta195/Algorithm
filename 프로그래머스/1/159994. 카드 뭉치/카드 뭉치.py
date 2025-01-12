def solution(cards1, cards2, goal):

    q = [(0, 0, 0)]
    while q:
        idx1, idx2, gidx = q.pop()
        if gidx == len(goal):
            return 'Yes'
        if idx1 < len(cards1) and cards1[idx1] == goal[gidx]:
            q.append((idx1+1, idx2, gidx+1))
        if idx2 < len(cards2) and cards2[idx2] == goal[gidx]:
            q.append((idx1, idx2+1, gidx+1))
    return 'No'