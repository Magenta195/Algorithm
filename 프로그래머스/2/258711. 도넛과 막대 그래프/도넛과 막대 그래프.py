from collections import deque
MAX = 10**6 + 1

def bfs(outdegree, visited, start) :
    q = deque([start])
    visited[start] = True
    while q :
        n = q.popleft()
        for m in outdegree[n] :
            if not visited[m] :
                visited[m] = True
                q.append(m)    

def solution(edges):
    answer = [0]*4
    indegree = [0]*MAX
    outdegree = [list() for _ in range(MAX)]
    visited = [True]*MAX
    
    for a, b in edges :
        indegree[b] += 1
        outdegree[a].append(b)
        visited[a] = visited[b] = False
        
    for i in range(1, MAX) :
        if indegree[i] == 0 and len(outdegree[i]) > 1 :
            answer[0] = i
            visited[i] = True
            for j in outdegree[i] :
                indegree[j] -= 1
            break
    
    for i in range(1, MAX) :
        if visited[i] :
            continue
        if indegree[i] == 0 :
            bfs(outdegree, visited, i)
            answer[2] += 1
        elif indegree[i] == len(outdegree[i]) == 2 :
            bfs(outdegree, visited, i)
            answer[3] += 1
    
    for i in range(1, MAX) :
        if visited[i] :
            continue
        bfs(outdegree, visited, i)
        answer[1] += 1
    
    return answer