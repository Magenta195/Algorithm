import sys
input = sys.stdin.readline

def preprocess():
  global s_c
  jump = [-1]*s_c
  stk = []
  for i in range(s_c):
    if program[i] == '[':
      stk.append(i)
    if program[i] == ']':
      j = stk.pop()
      jump[i] = j
      jump[j] = i

  return jump
  
def interpreter(t):
  global pointer, idx, input_idx, s_m, s_c, s_i, min_idx, max_idx
  if program[idx] == '-':
    arr[pointer] = (arr[pointer]-1)%256
  elif program[idx] == '+':
    arr[pointer] = (arr[pointer]+1)%256
  elif program[idx] == '<':
    pointer = (pointer-1)%s_m
  elif program[idx] == '>':
    pointer = (pointer+1)%s_m
  elif program[idx] == '[':
    if arr[pointer] == 0 : idx = jump[idx]
  elif program[idx] == ']':
    if arr[pointer] != 0 : idx = jump[idx]
  elif program[idx] == ',':
    arr[pointer] = ord(inputs[input_idx]) if input_idx < s_i else 255
    input_idx += 1
  
  idx += 1
  if t > 50000000:
    min_idx = min(min_idx, idx)
    max_idx = max(max_idx, idx)
  
  return pointer, idx, input_idx
  
T = int(input())

for _ in range(T):
  s_m, s_c, s_i = map(int, input().split())
  program = input().strip()
  inputs = input().strip()
  arr = [0]*s_m
  
  jump = preprocess()
  pointer, idx, input_idx, t = 0, 0, 0, 0
  min_idx = max_idx = 0
  looped = True
  while idx < s_c :
    if t == 50000000:
      min_idx = max_idx = idx
    if t >= 100000000 :
      print("Loops", min_idx-1, max_idx)
      break
      
    t += 1
    pointer, idx, input_idx = interpreter(t)
  if idx == s_c : print("Terminates")