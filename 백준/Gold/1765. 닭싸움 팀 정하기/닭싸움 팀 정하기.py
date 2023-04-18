import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = list(range(N))

def find(a) :
  if a == parent[a] :
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(a, b) :
  pa = find(a)
  pb = find(b)

  if pa <= pb :
    parent[pb] = pa
  else :
    parent[pa] = pb

def init() :
  adj_dict = { key : 
      { 'E' : list() , 'F' : list() }
      for key in range(N)
  }

  for _ in range(M) :
    typ, p, q = input().split()
    p, q = int(p)-1, int(q)-1

    adj_dict[p][typ].append(q)
    adj_dict[q][typ].append(p)
  return adj_dict

def ismatch(a, b, adj_dict) :
    for i in adj_dict[a]['E'] :
        for j in adj_dict[b]['E'] :
            if i == j :
                return True
    if b in adj_dict[a]['F'] and a in adj_dict[b]['F'] :
        return True
    
    return False
    
def full_search(adj_dict) :
  for i in range(N-1) :
    for j in range(i+1, N) :
      if ismatch(i, j, adj_dict):
        union(i, j)

  for i in range(N) :
    find(i)

  print(len(set(parent)))

def solve() :
  adj_dict = init()
  full_search(adj_dict)

solve()