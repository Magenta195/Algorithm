


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
MAX = float('inf')


def move_A(board, cnt, aloc, bloc) :
    global N, M
    
    ar, ac = aloc
    if board[ar][ac] == 0 :
        return False, cnt
    
    board[ar][ac] = 0
    is_movable = False
    win_cnt = 0
    min_cnt, max_cnt = MAX, -MAX
    
    for k in range(4) :
        _ar, _ac = ar + dr[k], ac + dc[k]
        if -1 < _ar < N and -1 < _ac < M and board[_ar][_ac] :
            is_b_win, _cnt = move_B(board, cnt+1, [_ar, _ac], bloc)
            is_movable = True
            if is_b_win :
                max_cnt = max(max_cnt, _cnt)
            else :
                win_cnt += 1
                min_cnt = min(min_cnt, _cnt)
            
            
    board[ar][ac] = 1
    if not is_movable :
        return False, cnt
    if not win_cnt :
        return False, max_cnt
    return True, min_cnt
    
def move_B(board, cnt, aloc, bloc) :
    global N, M
    
    br, bc = bloc
    if board[br][bc] == 0 :
        return False, cnt
    
    board[br][bc] = 0
    is_movable = False
    win_cnt = 0
    min_cnt, max_cnt = MAX, -MAX
    
    for k in range(4) :
        _br, _bc = br + dr[k], bc + dc[k]
        if -1 < _br < N and -1 < _bc < M and board[_br][_bc] :
            is_a_win, _cnt = move_A(board, cnt+1, aloc, [_br, _bc])
            is_movable = True
            if is_a_win :
                max_cnt = max(max_cnt, _cnt)
            else :
                win_cnt += 1
                min_cnt = min(min_cnt, _cnt)
                
    board[br][bc] = 1
    if not is_movable :
        return False, cnt
    if not win_cnt :
        return False, max_cnt
    return True, min_cnt

def solution(board, aloc, bloc):
    global N, M 
    N, M = len(board), len(board[0])

    _, cnt = move_A(board, 0, aloc, bloc)
    
    return cnt