from collections import defaultdict

def solution(points, routes):
    try :
        cur = []
        visited = defaultdict(int)
        for i in range(len(routes)) :
            cur.append((i, 0, *points[routes[i][0]-1]))
            visited[tuple(points[routes[i][0]-1])] += 1

        answer = sum(map(lambda x : x > 1, visited.values()))
        final = len(routes[0])-1
        while cur :
            nxt = []
            visited = defaultdict(int)
            for i, j, r, c, in cur :
                if j == final :
                    continue
                nr, nc = points[routes[i][j+1]-1]
                if nr > r :
                    ar, ac = r+1, c
                elif nr < r :
                    ar, ac = r-1, c
                elif nc > c :
                    ar, ac = r, c+1
                else :
                    ar, ac = r, c-1
                if (nr, nc) == (ar, ac) :
                    j += 1
                visited[(ar, ac)] += 1
                nxt.append((i, j, ar, ac))
            answer += sum(map(lambda x : x > 1, visited.values()))
            cur = nxt

        return answer
    except :
        return 0