codebook = {
    'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3
}

def solution(data, ext, val_ext, sort_by):
    answer = [ d for d in data if d[codebook[ext]] < val_ext]
    answer.sort(key = lambda x : x[codebook[sort_by]])
    return answer