def solution(sequence, k):
    lidx, ridx = 0, 0
    answer = [-float('inf'), float('inf')]
    partial_sum = sequence[0]
    
    while lidx <= ridx < len(sequence) :
        if partial_sum == k :
            if (answer[1] - answer[0]) > ridx - lidx :
                answer = [lidx, ridx]
            
            ridx += 1
            if ridx < len(sequence) :
                partial_sum += sequence[ridx] - sequence[lidx]
            lidx += 1
        elif partial_sum > k :
            partial_sum -= sequence[lidx]
            lidx += 1
        else :
            ridx += 1
            if ridx < len(sequence) :
                partial_sum += sequence[ridx]
        
    return answer