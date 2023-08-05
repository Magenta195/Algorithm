from heapq import heappush, heappop, heapify
import sys

input = sys.stdin.readline


class maxstr():

  def __init__(self, string):
    self.string = string

  def __lt__(self, other):
    return self.string.__gt__(other.string)

  def __le__(self, other):
    return self.string.__ge__(other.string)

  def __eq__(self, other):
    return self.string.__eq__(other.string)


class directory():

  def __init__(self, S, parent, base):
    self.name = S
    
    self.maxfiles = list()
    self.minfiles = list()
    self.file_set = set()
    
    self.childs = dict()
    self.maxchild = list()
    self.minchild = list()
    self.parent = parent
    self.base = base

  def mkalb(self, S):
    if S in self.childs:
      return False
    else:
      heappush(self.minchild, S)
      heappush(self.maxchild, maxstr(S))
      self.childs[S] = directory(S, self,
              self.base if self.base is not None else self)
      return True

  def _rmalb(self, ):
    dir_result, file_result = 1, len(self.file_set)
    for key in self.minchild:
      if key not in self.childs :
        continue
      tdir, tfile = self.childs[key]._rmalb()
      dir_result += tdir
      file_result += tfile
      del self.childs[key]
    return dir_result, file_result

  def rmalb(self, option):
    dir_result, file_result = 0, 0
    if option in ['-1', '1']:
      if self.childs:
        if option == '-1':
          key = heappop(self.minchild)
          while key not in self.childs and self.minchild :
            key = heappop(self.minchild)
        else:
          key = heappop(self.maxchild).string
          while key not in self.childs and self.maxchild :
            key = heappop(self.maxchild).string
        dir_result, file_result = self.childs[key]._rmalb()
        del self.childs[key]
    elif option == '0':
      for key in self.minchild:
        if key not in self.childs :
          continue
        tdir, tfile = self.childs[key]._rmalb()
        dir_result += tdir
        file_result += tfile
        del self.childs[key]
      self.minchild = list()
      self.maxchild = list()
      self.childs = dict()
    else:
      if option in self.childs:
        dir_result, file_result = self.childs[option]._rmalb()
        del self.childs[option]
    return dir_result, file_result

  def insert(self, filename):
    if filename in self.file_set:
      return False
    else:
      heappush(self.minfiles, filename)
      heappush(self.maxfiles, maxstr(filename))
      self.file_set.add(filename)
      return True

  def delete(self, option):
    delete_num = 0
    if option in ['-1', '1']:
      if self.file_set:
        if option == '-1':
          key = heappop(self.minfiles)
          while key not in self.file_set and self.minfiles :
            key = heappop(self.minfiles)
        else:
          key = heappop(self.maxfiles).string
          while key not in self.file_set and self.maxfiles :
            key = heappop(self.maxfiles).string
        self.file_set.discard(key)
        delete_num += 1
    elif option == '0':
      delete_num += len(self.file_set)
      self.minfiles = list()
      self.maxfiles = list()
      self.file_set = set()
    else:
      if option in self.file_set:
        self.file_set.discard(option)
        delete_num += 1
    return delete_num

  def ca(self, option):
    if option == '..':
      return self.parent if self.parent != None else None
    elif option == '/':
      return self.base if self.base != None else None
    else:
      if option not in self.childs:
        return None
      else:
        return self.childs[option]


N = int(input())
base_album = directory('album', None, None)
cur_dir = base_album
for _ in range(N):
  func, option = input().split()
  if func == 'mkalb':
    result = cur_dir.mkalb(option)
    if not result:
      print('duplicated album name')
  elif func == 'rmalb':
    dir_result, file_result = cur_dir.rmalb(option)
    print(dir_result, file_result)
  elif func == 'insert':
    result = cur_dir.insert(option)
    if not result:
      print('duplicated photo name')
  elif func == 'delete':
    result = cur_dir.delete(option)
    print(result)
  elif func == 'ca':
    result = cur_dir.ca(option)
    if result is not None:
      cur_dir = result
    print(cur_dir.name)
