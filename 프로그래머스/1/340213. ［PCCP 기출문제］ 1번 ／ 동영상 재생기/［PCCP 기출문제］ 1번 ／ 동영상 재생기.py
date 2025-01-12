def time_to_num(string):
    m, s = string.split(':')
    return int(m)*60 + int(s)

def num_to_time(num):
    return str(num // 60).rjust(2, "0") + ':' + str(num % 60).rjust(2, "0")

def move_next(pos_num, video_len_num):
    return min(pos_num + 10, video_len_num)

def move_prev(pos_num):
    return max(pos_num - 10, 0)

def skipOp(pos_num, op_start_num, op_end_num):
    if op_start_num <= pos_num <= op_end_num:
        return op_end_num
    return pos_num

def solution(video_len, pos, op_start, op_end, commands):
    video_len_num = time_to_num(video_len)
    op_start_num = time_to_num(op_start)
    op_end_num = time_to_num(op_end)
    pos_num = time_to_num(pos)
    pos_num = skipOp(pos_num, op_start_num, op_end_num)
    
    for comm in commands :
        if comm == 'prev':
            pos_num = move_prev(pos_num)
        else :
            pos_num = move_next(pos_num, video_len_num)
        pos_num = skipOp(pos_num, op_start_num, op_end_num)
        
    return num_to_time(pos_num)