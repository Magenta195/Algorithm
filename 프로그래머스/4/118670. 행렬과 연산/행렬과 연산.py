from collections import deque

def shift_rows(left_rc, right_rc, center_rc):
    left_rc.rotate()
    right_rc.rotate()
    center_rc.rotate()
    return left_rc, right_rc, center_rc

def rotates(left_rc, right_rc, center_rc=None):
    if center_rc == None :
        right_rc.appendleft(left_rc.popleft())
        left_rc.append(right_rc.pop())
        return left_rc, right_rc
    
    right_rc.appendleft(center_rc[0].pop())
    center_rc[-1].append(right_rc.pop())
    left_rc.append(center_rc[-1].popleft())
    center_rc[0].appendleft(left_rc.popleft())
    
    return left_rc, right_rc, center_rc
    

def solution(rc, operations):
    col_length, row_length = len(rc), len(rc[0])
    left_rc = deque([rc[i][0] for i in range(col_length)])
    right_rc = deque([rc[i][-1] for i in range(col_length)])
    center_rc = deque([deque(rc[i][1:-1]) for i in range(col_length)])
    for ops in operations :
        if ops == "ShiftRow" :
            left_rc, right_rc, center_rc = shift_rows(left_rc, right_rc, center_rc)
        else :
            if row_length < 3 :
                left_rc, right_rc = rotates(left_rc, right_rc)
            else :
                left_rc, right_rc, center_rc = rotates(left_rc, right_rc, center_rc)
    
    new_rc = [[left_rc[i]] + list(center_rc[i]) + [right_rc[i]] for i in range(col_length)]

    return new_rc