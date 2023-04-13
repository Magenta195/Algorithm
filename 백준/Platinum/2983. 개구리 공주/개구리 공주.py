from collections import defaultdict
import sys
input = sys.stdin.readline

class Node:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dir = {
      'A' : None,
      'B' : None,
      'C' : None,
      'D' : None
    }



  
def init() :
  N, K = map(int, input().split())
  node_list = list()
  move_string = input().strip()

  for i in range(N) :
    x, y = map(int, input().split())
    node = Node(x, y)
    if i == 0:
      start = node
    node_list.append(node)

  node_list.sort( key = lambda nd : (nd.x - nd.y, nd.x))
  for i in range(1, N) :
    if node_list[i-1].x - node_list[i-1].y == node_list[i].x - node_list[i].y :
      node_list[i-1].dir['A'] = node_list[i]
      node_list[i].dir['D'] = node_list[i-1]

  node_list.sort( key = lambda nd : (nd.x + nd.y, nd.x))
  for i in range(1, N) :
    if node_list[i-1].x + node_list[i-1].y == node_list[i].x + node_list[i].y :
      node_list[i-1].dir['B'] = node_list[i]
      node_list[i].dir['C'] = node_list[i-1]

    
  return move_string, start
  
def remove(node, s1, s2) :
  if node.dir[s1] is not None and node.dir[s2] is not None :
    node.dir[s1].dir[s2], node.dir[s2].dir[s1] = node.dir[s2], node.dir[s1]
  elif node.dir[s1] is not None :
    node.dir[s1].dir[s2] = None
  elif node.dir[s2] is not None :
    node.dir[s2].dir[s1] = None

def jumps(move_string, node) :
  for s in move_string :
    if node.dir[s] is not None :  
      next_node = node.dir[s]
      remove(node, 'A', 'D')
      remove(node, 'C', 'B')
      node = next_node
      
  print(node.x, node.y)
  

def solve() :
  move_string, start = init()
  jumps(move_string, start)

solve()