def solution(board, h, w):
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        ah, aw = h + dh[i], w + dw[i]
        if -1 < ah < len(board) and -1 < aw < len(board[0]) and board[ah][aw] == board[h][w]:
            count += 1
    return count