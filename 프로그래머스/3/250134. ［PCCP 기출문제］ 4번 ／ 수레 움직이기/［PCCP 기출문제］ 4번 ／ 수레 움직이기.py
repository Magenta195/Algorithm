from collections import deque
import sys
sys.setrecursionlimit(100000)

MAX = float('inf')
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def solution(maze):
    N, M = len(maze), len(maze[0])
    for i in range(N) :
        for j in range(M) :
            if maze[i][j] == 1 :
                srr, src = i, j
            if maze[i][j] == 2 :
                sbr, sbc = i, j
            if maze[i][j] == 3 :
                err, erc = i, j
            if maze[i][j] == 4 :
                ebr, ebc = i, j
    
    r_visited = [[False]*M for _ in range(N)]
    b_visited = [[False]*M for _ in range(N)]
    r_visited[srr][src] = True
    b_visited[sbr][sbc] = True
    
    def dfs(rr, rc, br, bc, d) :
        if (rr, rc) == (err, erc) and (br, bc) == (ebr, ebc) :
            return d
        r_range = range(1) if (rr, rc) == (err, erc) else range(1, 5) 
        b_range = range(1) if (br, bc) == (ebr, ebc) else range(1, 5)
        result = MAX
        
        for i in r_range :
            arr, arc = rr + dr[i], rc + dc[i]
            if not (-1 < arr < N and -1 < arc < M) :
                continue
            if i > 0 and (r_visited[arr][arc] or maze[arr][arc] == 5 ) :
                continue
            if i > 0 :
                r_visited[arr][arc] = True
                
            for j in b_range :
                abr, abc = br + dr[j], bc + dc[j]
                if not (-1 < abr < N and -1 < abc < M) : 
                    continue
                if j > 0 and (b_visited[abr][abc] or maze[abr][abc] == 5 ) :
                    continue
                if (arr, arc) == (br, bc) and (abr, abc) == (rr, rc) :
                    continue
                if (arr, arc) == (abr, abc) :
                    continue
                if j > 0 :
                    b_visited[abr][abc] = True
                    
                result = min(result, dfs(arr, arc, abr, abc, d+1))
                
                if j > 0  :
                    b_visited[abr][abc] = False
            if i > 0 :
                r_visited[arr][arc] = False
                
        return result
    
    answer = dfs(srr, src, sbr, sbc, 0)
    
    return answer if answer < MAX else 0